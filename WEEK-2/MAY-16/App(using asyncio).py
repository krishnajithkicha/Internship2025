import asyncio
import autogen

# Defining model, API key, and API type for autogen
config_list = [
    {'model': 'gemini-1.5-flash',
     "api_type": "google",
     'api_key': 'AIzaSyDl7hvmtuosswT62ty3V-SDmrWXAy3Z-pE'}
]
# Setting configuration
llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

# Defining assistant agent for responding
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

# Defining user proxy for getting user input
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web", "use_docker": False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE or the reason why the task is not solved yet."""
)

task = """
Describe about Autogen AI in few sentences.
"""

# Asynchronous function to run the synchronous initiate_chat
async def initiate_task_async():
    await asyncio.to_thread(
        user_proxy.initiate_chat,
        assistant,
        message=task,
    )

# Entry point for the asyncio script
if __name__ == "__main__":
    asyncio.run(initiate_task_async())
