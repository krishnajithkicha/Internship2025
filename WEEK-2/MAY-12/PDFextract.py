#This program is to extract the contents from the pdf
import fitz #Importing the library PyMuPDF
#This function is to extract the text from the pdf
def extract_pdf_text(filepath): #Takes the file path as input
    doc=fitz.open(filepath) #Open the pdf file
    #Iterate through the pages of the pdf
    for i in range(len(doc)):
        page=doc.load_page(i) #Load the page
        print("Extracting PDF Document")
        print("Page Number:",i+1,"Contents are:")
        print(page.get_text()) #Extract the text from the page and printing it

pdf="example.pdf" #Path to the pdf file
extract_pdf_text(pdf)   #Calling the function to extract the text from the pdf