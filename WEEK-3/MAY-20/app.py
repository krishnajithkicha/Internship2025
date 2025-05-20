#creating two agents coder and debugger
#coder will generate code and debugger will debug the code
#debugger will use pylint to debug the code
#coder will use gemini to generate code
#debugger will use gemini to debug the code
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
from pylint.lint import Run


load_dotenv()
# Load environment variables from .env file
async def main():
    model_client = OpenAIChatCompletionClient (
        model="gemini-1.5-flash-8b",
        api_key=os.getenv("API_KEY") # Load from .env
)

#define the coder agent
    coder = AssistantAgent(
        name="Coder",
        model_client=model_client,
        description="Code generation agent",
        system_message="You are coding assistant.Your task is to provide the code.",
    )

    # Define the debugger agent
    debugger = AssistantAgent(
        name="Debugger",
        model_client=model_client,
        description=" Debugging assistant.",
        system_message="You are a helpful debugging assistant and your task is to validate and debug the code and when done debugging type Terminate.",
        
    )
    termination_condition=TextMentionTermination("Terminate")
    # Create a group chat with round-robin communication
    group_chat = RoundRobinGroupChat([coder, debugger],termination_condition=termination_condition)

    # Create a console UI for the group chat
    t=input("Enter the program to generate code for: ")
    await Console(group_chat.run_stream(task=t))

    await model_client.close()
# Run the main function
if __name__ == "__main__":
    asyncio.run(main())