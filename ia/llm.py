from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7  #coloquei 0.7 pq é o que está nos slides
)

#falta o prompt, que, pelo que eu entendi vai aqui