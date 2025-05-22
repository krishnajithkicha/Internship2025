import asyncio
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from queryhandler import QueryHandler
from RAGretriver import RAGRetriever
from dotenv import load_dotenv

load_dotenv()

async def main():
    model_client=OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        apikey=os.getenv("API_KEY")
    )

    queryhandler=AssistantAgent(
        name="QueryHandler",
        description="Handles user queries and forwards them to the RAG system.",
        model_client=model_client,
        system_message="You are Queryhandling agent,Your task is to facilitate user queries for RAG System"
    )

    RAGretriver=AssistantAgent(
        name="RAGRetriever",
        description="Uses ChromaDB and Gemini for RAG based response generation",
        model_client=model_client,
        system_message="You are RAGRetriever.Your task is to retrieve relevant data using ChromaDB and generate accurate response"
    )

    termination=TextMentionTermination("TERMINATE")
    group_chat=RoundRobinGroupChat(
        [queryhandler,RAGretriver],
        max_turns=5
    )

    user_query=input("Enter your query:")
    print("User query:",user_query)

    await Console(group_chat.run_stream(task=user_query))

if __name__=="__main__":
    asyncio.run(main())
