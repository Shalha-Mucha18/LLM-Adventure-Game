from sqlalchemy.orm import Session

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import PydanticOutputParser 

from core.config import setting
from models.story import StoryNode, Story
from schemas.llm import StoryLLMResponse , StoryNodeLLM, StoryOptionLLM
from core.prompt import system_prompt

class LLMAdapter:

    @classmethod
    def __get__llm(cls):
        api_key = setting.GROQ_API_KEY
        print(f"API Key loaded: {api_key[:10]}...{api_key[-10:] if len(api_key) > 20 else api_key}")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        llm = ChatGroq(api_key=api_key, model="llama-3.1-8b-instant", temperature=0.3)
        return llm
    @classmethod

    def generate_story(cls, db:Session, session_id:str,theme:str = "avenger") -> Story:

        llm = cls.__get__llm()


        
        prompt = ChatPromptTemplate.from_messages([
           ("system", system_prompt),
            (
                "user", 
                f"Create the story with this theme: {theme}"
            )
        ])

        formatted_prompt = prompt.invoke({})
        print(f"Sending prompt: {formatted_prompt}")
        
        response = llm.invoke(formatted_prompt)
        print(f"Raw LLM response: {response}")

        response_text = response

        if hasattr(response, 'content'):
            response_text = response.content
            print(f"Response content: {response_text}")
        
        if not response_text:
            raise ValueError(f"Empty response from LLM: {response}")

        # Extract and parse JSON from response
        import json
        import re
        
        # Find JSON object in the response
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            print(f"Extracted JSON: {json_str[:200]}...")
            
            # Clean JSON - remove comments and fix common issues
            json_str = re.sub(r'//.*?\n', '\n', json_str)  # Remove // comments
            json_str = re.sub(r'/\*.*?\*/', '', json_str, flags=re.DOTALL)  # Remove /* */ comments
            json_str = json_str.replace('null', 'None').replace('None', 'null')  # Ensure proper null
            
            try:
                # Parse JSON directly
                story_data = json.loads(json_str)
                story_structure = StoryLLMResponse.model_validate(story_data)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                print(f"Problematic JSON: {json_str}")
                raise ValueError(f"Invalid JSON from LLM: {e}")
        else:
            raise ValueError(f"No valid JSON found in response: {response_text[:200]}...")

        story_db = Story(title=story_structure.title, session_id=session_id)
        db.add(story_db)
        db.flush()


        root_node_data = story_structure.rootNode
        if isinstance(root_node_data,dict):
            root_node_data = StoryNodeLLM.model_validate(root_node_data)

        cls.__process_stroy_node(db, story_db.id, root_node_data, is_root=True)
        return story_db
    

    @classmethod
    def __process_stroy_node(cls, db:Session, story_id:int, node_data:StoryNodeLLM, is_root:bool=False) -> StoryNode:
          
          node = StoryNode(
            story_id=story_id,
            content=node_data.content,
            is_root=is_root,
            is_ending=node_data.isEnding,
            is_winning_ending=node_data.isWinningEnding,
            options=[]
          )
          db.add(node)
          db.flush()

          if not node_data.isEnding and node_data.options:
            options_list = []
            for option_data in node_data.options:
                next_node = option_data.nextNode

                if isinstance(next_node,dict):
                    next_node = StoryNodeLLM.model_validate(next_node)

                child_node = cls.__process_stroy_node(db,story_id, next_node, is_root=False)    
                options_list.append({
                    "text": option_data.text,
                    "nextNodeId": child_node.id
                })
            node.options = options_list
            db.flush()
          
          return node



