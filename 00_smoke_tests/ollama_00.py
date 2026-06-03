from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="phi3:mini")
print(llm.invoke("Hola, ¿qué puedes hacer?"))