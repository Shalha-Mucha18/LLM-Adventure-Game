system_prompt = """
Create a simple choose-your-own-adventure story in JSON format.

Requirements:
- Keep it SHORT and simple
- Root node with 2 options only
- Each option leads to an ending (win or lose)
- Maximum 2 levels deep

Example structure:
{{
  "title": "Short Adventure",
  "rootNode": {{
    "content": "You face a challenge.",
    "isEnding": false,
    "isWinningEnding": false,
    "options": [
      {{
        "text": "Choice A",
        "nextNode": {{
          "content": "You win!",
          "isEnding": true,
          "isWinningEnding": true,
          "options": null
        }}
      }},
      {{
        "text": "Choice B", 
        "nextNode": {{
          "content": "You lose.",
          "isEnding": true,
          "isWinningEnding": false,
          "options": null
        }}
      }}
    ]
  }}
}}

Return ONLY valid JSON.
"""

json_structure = """
        {
            "title": "Story Title",
            "rootNode": {
                "content": "The starting situation of the story",
                "isEnding": false,
                "isWinningEnding": false,
                "options": [
                    {
                        "text": "Option 1 text",
                        "nextNode": {
                            "content": "What happens for option 1",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    // More options for root node
                ]
            }
        }
        """

