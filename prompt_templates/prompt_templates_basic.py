from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

#create the template
template = "Tell me a joke about {topic}"
prompt_template = ChatPromptTemplate.from_template(template)

#create the prompt 
prompt = prompt_template.invoke({"topic":"sex"})
print(prompt)

#prompt with human and sytems messages
messages = [
    ("system", "you are a {role}"),
    ("human", "what is 1 + {n}"),
]
prompt_template = ChatPromptTemplate.from_messages(messages)

prompt = prompt_template.invoke({"role":"math teacher", "n":"2"})

print(prompt)

'''
#Or you can write it like that 
#prompt with human and sytems messages
messages = [
    ("system", "you are a {role}"),
    HumanMessage(content="what is 1 + 1"),
]
prompt_template = ChatPromptTemplate.from_messages(messages)

prompt = prompt_template.invoke({"role":"math teacher", "n":"2"})

print(prompt)
'''
