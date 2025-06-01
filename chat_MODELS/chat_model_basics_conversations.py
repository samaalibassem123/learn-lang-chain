from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")


# Think of it as messages history
messages = [
    SystemMessage(content="""- you are a math teacher
                  - be kind"""), # define how to ai behave or think
    HumanMessage(content="who are u"), # user message
    AIMessage("im math teacher trying to help "), # ai response
    HumanMessage(content="how are u"),# new user message
    
]

res = llm.invoke(messages)
print(res.content)