import asyncio

class QueryHandler:
    def __init__(self):
        pass

    async def query_process(self,query):
        await asyncio.sleep(1)
        print(f"Processing query:{query}")
        return query
    
    
