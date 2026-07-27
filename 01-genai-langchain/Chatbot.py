from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import AIMessage,HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

chain = model | parser
history=[
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("You: ")
    history.append(HumanMessage(content=user_input))

    if user_input.lower() == "exit":
        break

    answer = chain.invoke(history)
    history.append(AIMessage(content=answer))
    print("AI:", answer)

print(history)