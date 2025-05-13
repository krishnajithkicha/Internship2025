#This program is to show how gemini api works
import google.generativeai as genai #importing the google generative ai library

def call_gemini(api_key,prompt): #Calling the gemini api
    genai.configure(api_key=api_key) #Configuring the api key
    model=genai.GenerativeModel("gemini-1.5-flash")  #Creating the model object
    return model.generate_content(prompt) #Generating the content using the prompt

def text_summarization(api_key,text): #Summarizing the text
    genai.configure(api_key=api_key)
    model=genai.GenerativeModel("gemini-1.5-flash") 
    return model.generate_content(f"Summarize:{text}")  #Summarizing the text

def question_answering(api_key,question,content): #Answering the question
    genai.configure(api_key=api_key)
    model=genai.GenerativeModel("gemini-1.5-flash")
    return model.generate_content(f"Question:{question} Content:{content}") #Answering the question

api_key="AIzaSyDONmtUGAnymnErP5R63fjN9tzh_Ch6ftY" #API KEY DEFINED
prompt="A short note on gemini ai"
res=call_gemini(api_key,prompt)
print("Gemini AI response for content generation:")
print(res)
text="Prompt engineering is the process of structuring or crafting an instruction in order to produce the best possible output from a generative artificial intelligence (AI) model."
print("Gemini AI response for text summarization:")
sum=text_summarization(api_key,text)
print(sum)
question="What is prompt?"
ans=question_answering(api_key,question,text)
print("Gemini AI response for question answering:")
print(ans)