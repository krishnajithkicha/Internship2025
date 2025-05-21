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
from pylint.reporters.text import TextReporter
from io import StringIO



load_dotenv()
# Load environment variables from .env file
def run_pylint(code:str)->str:
    tmp_file="temp_code.py"
    with open (tmp_file, "w") as f:
        f.write(code)
    output=StringIO()
    reporter=TextReporter(output=output)
    try:
        Run([tmp_file],reporter=reporter,do_exit=False)

    except Exception as e:
        return f"Pylint failed {e}"
    return output.getvalue()




async def main():
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key=os.getenv("API_KEY")  # Load from .env
    )

    #define the coder agent
    coder = AssistantAgent(
        name="Coder",
        model_client=model_client,
        description="Code generation agent",
        system_message="You are a helpful coding assistant.",
    )

    # Define the debugger agent
    debugger = AssistantAgent(
        name="Debugger",
        model_client=model_client,
        description="You are a helpful debugging assistant.",
        system_message=(
            "You're a Python debugger. Given Python code, use the function `run_pylint(code: str) -> str` "
            "to find issues. Then, rewrite or suggest fixes. When the code is clean, type 'Terminate'."
        )
    )

    termination_condition = TextMentionTermination("Terminate")
    group_chat = RoundRobinGroupChat([coder, debugger], termination_condition=termination_condition)

    t = input("Enter the program to generate code for: ")
    await Console(group_chat.run_stream(task=t))

    await model_client.close()

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())