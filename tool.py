import sys
import json
import asyncio
import traceback
from gptscript import GPTScript, Options


async def main():
    # Set up GPTScript client
    client = GPTScript()

    # Create system prompt input
    sys_prompt = {
        "message": "Please enter your Obot Hackathon Votes.",
        "fields": [
            {
                "name": "First Place",
                "sensitive": False,
                "description": "This selection will be awarded 3 points"
            },
            {
                "name": "Second Place",
                "sensitive": False,
                "description": "This selection will be awarded 2 points"
            },
            {
                "name": "Third Place",
                "sensitive": False,
                "description": "This selection will be awarded 1 point"
            }
        ]
    }

    try:
        # Run GPTScript with the system prompt and get response
        res = await client.run(
            "sys.prompt", 
            Options(input=json.dumps(sys_prompt))
        ).text()
        
        print(res)

    except Exception as err:
        print(f"Error: {err}")
        print("Full stack trace:")
        print(traceback.format_exc())
        sys.exit(1)

if __name__ == '__main__':
    asyncio.run(main())
