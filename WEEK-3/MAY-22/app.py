import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import chromadb
from chromadb.config import Settings

# Load environment variables
load_dotenv()

# === Initialize ChromaDB client ===
client = chromadb.PersistentClient(
    path=".chroma_db",
)
collection = client.get_or_create_collection(name="FAQ")

# === FAQ Add Tool ===
async def add_faq_to_chromadb(question: str, answer: str):
    """Add a question-answer pair as a document."""
    try:
        collection.add(
            documents=[{"content": answer}],
            metadatas=[{"question": question}],
            ids=[question]
        )
        return f"✅ FAQ added: {question}"
    except Exception as e:
        return f"❌ Error adding FAQ: {str(e)}"

# === RAG Retrieval Tool ===
async def retrieve_answer_from_faq(question: str) -> str:
    """Retrieve an answer based on semantic document search."""
    try:
        results = collection.query(query_texts=[{"content": question}], n_results=1)
        if results and results['documents'] and results['documents'][0]:
            return results['documents'][0][0]["content"]  # Return top document content
        return "❓ Sorry, I don't have an answer to that question yet."
    except Exception as e:
        return f"❌ Error during retrieval: {str(e)}"

# === Main async entry ===
async def main():
    print("🔄 Initializing Gemini-powered FAQ Chatbot...")

    # Initialize the Gemini model client
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key=os.getenv("API_KEY")  # Ensure API_KEY is in your .env file
    )

    # === Agents ===

    # RAG Retriever Agent
    retriever_agent = AssistantAgent(
        name="RAGRetriever",
        model_client=model_client,
        description="Retrieves answers from ChromaDB using semantic search.",
        system_message="""
You are an FAQ assistant. Follow these exact steps:

1. Use the retrieve_answer_from_faq tool with the user's question.
2. If the result is:
   - Missing, or
   - Starts with "❓ Sorry"
Then:
   - Use your own knowledge to generate the correct answer.
   - Use add_faq_to_chromadb to save the question and your generated answer.
3. Then reply to the user with the final answer.
4. Finish your message with "TERMINATE" (to end the session).

Be sure to execute all needed tools in order. Do not stop after the first step.
""",
        tools=[retrieve_answer_from_faq, add_faq_to_chromadb]
    )

    # Query Handler Agent
    query_handler = AssistantAgent(
        name="QueryHandler",
        model_client=model_client,
        description="Answers user questions by using RAGRetriever results.",
        system_message="""
Your job is to call add_faq_to_chromadb when the user provides a new FAQ (question + answer).
If you're unsure whether it’s a new FAQ or a query, delegate to the RAGRetriever.
""",
        tools=[add_faq_to_chromadb]
    )

    # User Proxy Agent
    user = UserProxyAgent(
        name="User",
        description="The user who asks FAQ-related questions or submits new FAQs."
    )

    # === Group Chat Setup ===
    termination = TextMentionTermination("TERMINATE")
    group_chat = RoundRobinGroupChat(
        [user, query_handler, retriever_agent],
        termination_condition=termination
    )

    # === Run the Chat ===
    print("✅ Chatbot initialized. Starting session...\n")
    await Console(group_chat.run_stream(task="Submit a question or a document for FAQ assistance."))

    await model_client.close()

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
