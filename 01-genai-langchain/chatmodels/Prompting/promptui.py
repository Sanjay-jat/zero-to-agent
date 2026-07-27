from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

llm1=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm1)


st.header('Research Tool')

user_input=st.text_input('Enter you query')

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.write(result.content)
    

