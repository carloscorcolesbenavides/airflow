from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3:mini",
    base_url="http://localhost:36813"
)
response = llm.invoke("Hola, ¿qué puedes hacer?")
print(response.content)