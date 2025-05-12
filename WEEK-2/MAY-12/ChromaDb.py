#This is a simple example of how to use chromadb
import chromadb #Importing the library

documents=[     #This is the list of documents to be added to the database
    "This is a chromadb testing document",
    "This is a vector database",
    "This is amazing"
]
metadatas=[   #This is the list of metadata to be added to the database
    {"source":"intro1"},
    {"source":"intro2"},
    {"source":"intro3"}
]
ids=["id1","id2","id3"] #This is the list of ids to be added to the database
chroma_client=chromadb.Client() #Creating a client instance to connect to the database
collection=chroma_client.create_collection(name="sampledoc") #Creating a collection in the database
#Adding the documents to the collection
collection.add(documents=documents,metadatas=metadatas,ids=ids)
for i in range(len(ids)): #Iterating through the ids
    results=collection.get(ids=[ids[i]]) #Getting the results from the collection
    print("ID:",results["ids"][0]) #Printing the id
    print("Document:",results["documents"][0]) #Printing the document
    print("Metadata:",results["metadatas"][0]) #Printing the metadata
client=chromadb.PersistentClient(path="sampledocument") #Creating a persistent client instance to connect to the database
print("Heartbeat:",client.heartbeat()) #Printing the heartbeat of the client
