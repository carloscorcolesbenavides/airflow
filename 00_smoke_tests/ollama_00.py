from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3:mini")
response = llm.invoke("Hola, ¿qué puedes hacer?")
print(response.content)