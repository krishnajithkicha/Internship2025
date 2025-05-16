import autogen



config_list = [
    {'model':'gemini-1.5-flash', 
     "api_type":"google",
     'api_key':'AIzaSyDl7hvmtuosswT62ty3V-SDmrWXAy3Z-pE'}
]  

llm_config={
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,  #lower the temperature for less creative and less unique replies higher temperature for more creative and unique replies
     
}

assistant=autogen.AssistantAgent(
    name="assistant",     #we can also  add more number of agents
    llm_config=llm_config
    #if adding more than one agent we have to define system message to specify the roles
)

user_proxy=autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,   #if this value is too high there is a risk of infinite loop
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir":"web","use_docker":False},
    llm_config=llm_config,  
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.Otherwise, reply CONTINUE or the reason why the task is not solved yet."""
)
                      #agent that acts on behalf of the user

task="""
write a python script that takes a list of numbers and returns the sum of the even numbers in the list.
The script should be able to handle both positive and negative numbers.
"""

user_proxy.initiate_chat(
    assistant,
    message=task,
)