import asyncio
import pandas as pd
import os
import matplotlib.pyplot as plt
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from dotenv import load_dotenv

load_dotenv()

async def fetch_csv(file_path:str)->pd.DataFrame:
    await asyncio.sleep(1)
    return pd.read_csv(file_path)

async def analyze_data(data:pd.DataFrame,output_file:str):
    await asyncio.sleep(1)
    required_columns=["Category","UnitPrice"]
    
    plt.figure(figsize=(10,6))
    data.plot(kind="bar",x="Category",y="UnitPrice")
    plt.title("Data Visualization")
    plt.savefig(output_file)
    plt.close()

async def main():
    model_client=OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key=os.getenv("APIKEY")
    )

    data_fetcher=AssistantAgent(
        name="DataFetcher",
        description="Fetches CSV data and return as Dataframes",
        model_client=model_client,
        system_message="You are data fetching agent,Your task to fetch the data from csv and return as Dataframe"
    )

    analyst=AssistantAgent(
        name="Analyzer",
        description="Analyze the data and create visualization",
        model_client=model_client,
        system_message="You are analyst agent,Your task to analyze the data and create visualization"
    )

    termination=TextMentionTermination("TERMINATE")
    group_chat=RoundRobinGroupChat(
        [data_fetcher,analyst],
        max_turns=3
    )

    filepath="data/Sales.csv"
    output_file="output/visualization.png"
    data=await fetch_csv(filepath)
    print("Data fetched")

    await analyze_data(data,output_file)
    await Console(group_chat.run_stream(task=f"Analyze the data and visualize results for {filepath}"))

if __name__ == "__main__":
    asyncio.run(main())
