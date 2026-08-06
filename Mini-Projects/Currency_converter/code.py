from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import AIMessage,HumanMessage,SystemMessage,ToolMessage
import requests
from dotenv import load_dotenv
load_dotenv()
import os
API_KEY = os.getenv("API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)
@tool
def currency_factor(base_currency: str, target_currency: str) -> float:
    """This tool takes two currency codes as input and returns the conversion factor between them."""

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"

    response = requests.get(url)
    response.raise_for_status() 

    return response.json()

currency_result=currency_factor.invoke({"base_currency":"USD","target_currency":"INR"})
#print(currency_result)

@tool
def convert_currency(base_currency_value: int, conversion_rate: float) -> float:
    """Converts amount from one currency to another using the latest exchange rate."""
    return base_currency_value * conversion_rate

converted_currency=convert_currency.invoke({"base_currency_value":100,"conversion_rate":currency_result["conversion_rate"]})
#print(f"Converted currency: {converted_currency}")



llm_max=llm.bind_tools([convert_currency,currency_factor])

query=HumanMessage(content="what is the conversion factor between USD and INR and convert 50 USD to INR")  

messages = [query]

while True:
    ai_message = llm_max.invoke(messages)
    messages.append(ai_message)

    if not ai_message.tool_calls:
        break

    for tool_call in ai_message.tool_calls:
        if tool_call["name"] == "currency_factor":
            result = currency_factor.invoke(tool_call["args"])

        elif tool_call["name"] == "convert_currency":
            result = convert_currency.invoke(tool_call["args"])

        messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"],
            )
        )

final_response = messages[-1]

answer = final_response.content[0]["text"]
print(answer)