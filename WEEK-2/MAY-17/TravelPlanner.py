import autogen
import os
from dotenv import load_dotenv

load_dotenv()

config_list = [
    {
        'model': 'gemini-1.5-flash',
        'api_key': os.getenv("API_KEY"),  # Load from .env
        'api_type': 'google'
    }
]
print("API_KEY from env:",os.getenv("API_KEY"))  # Debugging line to check if API key is loaded correctly

llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0.7,
}

# Define the agents
planner_agent = autogen.AssistantAgent(
    name="planner_agent",
    llm_config=llm_config,
    system_message="You are a helpful assistant that can suggest a travel plan for a user based on their request."
)

local_agent = autogen.AssistantAgent(
    name="local_agent",
    llm_config=llm_config,
    system_message="You are a helpful assistant that can suggest authentic and interesting local activities or places to visit for a user."
)

language_agent = autogen.AssistantAgent(
    name="language_agent",
    llm_config=llm_config,
    system_message="You are a helpful assistant that provides tips for language and communication challenges for travelers."
)

summary_agent = autogen.AssistantAgent(
    name="travel_summary_agent",
    llm_config=llm_config,
    system_message="You are a helpful assistant that integrates all suggestions into a final detailed travel plan. When complete, respond with TERMINATE."
)

# User Proxy Agent to control termination
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved fully. Otherwise, reply CONTINUE or explain why it's not solved yet.""",
    code_execution_config={"use_docker": False}
)

# Define task
task = "Plan a 3-day trip to Nepal."

# Initiate chat flow
group_chat = autogen.GroupChat(
    agents=[planner_agent, local_agent, language_agent, summary_agent],
    messages=[],
    max_round=10
)
manager = autogen.GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)

user_proxy.initiate_chat(
    manager,
    message=task
)