from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):

    text: str = Field(description="The text of the option")
    nextNode: Dict[str, Any] = Field(description="The next node that this option leads to")




class StoryNodeLLM(BaseModel):
    content: str = Field(description="The content of the story node")
    isEnding: bool = Field(default=False, description="Indicates if this node is an ending")
    isWinningEnding: bool = Field(default=False, description="Indicates if this node is a winning ending")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="List of options leading to next nodes")


class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM = Field(description="The root node of the story")  