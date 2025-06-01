from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

#load enviroment variables
load_dotenv()



# Create an instance of the LLM, using the 'gemini-pro' model with a specified creativity level
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")

# Send a creative prompt to the LLM
response = llm.invoke("Hi")
print(response.content)