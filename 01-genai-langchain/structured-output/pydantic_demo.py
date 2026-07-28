
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated
from pydantic import BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class review(BaseModel):
    summary:Annotated[str,"A brief summary on topic"]
    sentiment:Annotated[str,"A sentiment analysis on topic"]

structured_model=model.with_structured_output(review)

result=structured_model.invoke("""Electric cars are growing fast on our roads. Many drivers love them because they save money on gas and do not pollute the air. But other people worry that charging stations are too hard to find, and fixing a broken battery costs too much money.""")

print(result)