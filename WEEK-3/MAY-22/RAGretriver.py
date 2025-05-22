import chromadb
import asyncio

class RAGRetriever:
    def __init__(self):
        self.client=chromadb.Client()
        self.collection=self.get_or_create_collection("faq_data")

    async def add_data(self,documents):
        for doc in documents:
            self.collection.add(doc)

    async def retrieve_and_generate(self,query):
        await asyncio.sleep(1)
        results=self.collection.query(query_texts=[query],n_results=3)
        print(f"Retrieved results :{results}")
        return f"Generated response for query:{query}"