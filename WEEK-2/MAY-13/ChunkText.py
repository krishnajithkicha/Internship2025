#This program is to show how to chunk a pdf file into smaller chunks
import fitz

def extract_pdf(filepath): #Extracting text from pdf
    doc=fitz.open(filepath)
    text=""
    for i in range(len(doc)):
        page=doc.load_page(i) #Loading the page
        text+=page.get_text()  #Extracting the text from the page
    doc.close() #Closing the document
    return text
def chunk_text(text,chars): #Chunking the text into smaller chunks
    chunks=[] 
    chunk_size=chars #Size of the chunk
    #Iterating through the text and creating chunks
    for i in range(0,len(text),chunk_size):
        chunk=text[i:i+chunk_size]  #Creating the chunk
        chunks.append(chunk)    #Adding the chunk to the list
    return chunks
file="example.pdf"
text=extract_pdf(file) #Extracting the text from the pdf
ch=chunk_text(text,500) #Chunking the text into smaller chunks
print("The text is chunked into smaller chunks of 500 characters each as list:")
print(ch)
print("The text is chunked into smaller chunks of 500 characters each:")
for i in range(len(ch)):
    print(f"Chunk {i+1}:")
    print(ch[i]) #Printing the chunk
    print("\n")
