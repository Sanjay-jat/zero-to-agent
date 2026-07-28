from dotenv import load_dotenv

from langchain.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

MODEL_NAME = "gemini-3.6-flash"

model = ChatGoogleGenerativeAI(model=MODEL_NAME)

parser = StrOutputParser()

chain = model | parser
# Conversation history
history = [
    SystemMessage(
        content="You are a helpful AI assistant."
    )
]


while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("\nGoodbye! 👋")
        break

    if not user_input:
        continue

    history.append(
        HumanMessage(content=user_input)
    )

    response = chain.invoke(history)

    history.append(
        AIMessage(content=response)
    )

    print(f"\nAI: {response}\n")


print("\nConversation History:\n")

for message in history:
    print(message)