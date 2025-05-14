import streamlit as st
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file
api_key = os.getenv("GOOGLE_API_KEY")   # Set up Google Generative AI API key
genai.configure(api_key=api_key) 

# Extract text from PDFs using PyMuPDF
def extract_pdf(pdf_docs):
    text=""
    for pdf in pdf_docs: # Loop through each PDF file and allow multiple uploads
        with fitz.open(stream=pdf.read(),filetype="pdf") as docs:
            for i in range(len(docs)):
                page=docs.load_page(i) # Load each page of the PDF
                text+=page.get_text() # Extract text from the page
    return text


# Split text into chunks
def extract_chunks(text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000) # Define chunk size and overlap
    chunks=text_splitter.split_text(text) # Split the text into chunks
    return chunks

# Store text chunks in ChromaDB
def store_vector(text_chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001") # Initialize embeddings
    vector_store=Chroma.from_texts(text_chunks,embedding=embeddings,persist_directory="chroma_index") # Create ChromaDB vector store
    vector_store.persist() # Persist the vector store or saving it to disk

# Create conversational chain
def conversational_chain():
    prompt_template="""
    Answer the question as detailed as possible from the provided context. 
    If the answer is not in the provided context, just say, 
    'Answer is not available in the context', don't provide a wrong answer.\n\n
    Context:\n {context}\n
    Question:\n {question}\n
    Answer:
    """
    model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3) # Initialize the model
    prompt=PromptTemplate(template=prompt_template,input_variables=["context", "question"]) # Create prompt template
    # Load the QA chain with the model and prompt
    chain=load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Process user questions
def user_question(user_input):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001") # Initialize embeddings
    # Load the vector store from the persisted directory
    vector_store=Chroma(persist_directory="chroma_index", embedding_function=embeddings)
    # Perform similarity search to find relevant documents based on user input
    docs=vector_store.similarity_search(user_input)
    chain=conversational_chain() # Create the conversational chain
    # Generate a response using the chain
    response=chain({"input_documents": docs, "question": user_input}, return_only_outputs=True)
    st.write("Response:", response["output_text"])

# Streamlit application
def main():
    st.set_page_config(page_title="Chat PDF", layout="wide")
    st.header("Chat with PDF using Gemini 💁")

    user_input = st.text_input("Ask a question from the uploaded PDFs:")
    if user_input:
        user_question(user_input)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files:", accept_multiple_files=True, type=["pdf"])
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = extract_pdf(pdf_docs)
                    text_chunks = extract_chunks(raw_text)
                    store_vector(text_chunks)
                    st.success("Processing complete!")
            else:
                st.warning("Please upload at least one PDF file.")

if __name__ == "__main__":
    main()
