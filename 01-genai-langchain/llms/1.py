from langchain_openai import OpenAI

from dotenv import load_dotenv
load_dotenv()
llm=OpenAI(model_name="gpt-3.5-turbo-instruct")

result=llm.invoke("what is the capital of india")
print(result)