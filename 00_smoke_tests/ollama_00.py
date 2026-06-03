from langchain_community.chat_models import ChatOllama

# Cambia 36813 por el puerto real que viste en ps aux
llm = ChatOllama(
    model="phi3:mini",
    base_url="http://localhost:36813"
)

print(llm.invoke("Hola, ¿qué puedes hacer?"))
