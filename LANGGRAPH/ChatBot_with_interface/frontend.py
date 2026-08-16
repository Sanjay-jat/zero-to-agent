import streamlit as st
from backend import chatbot
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
thread_id='1'
config1={'configurable':{'thread_id':thread_id}}
st.title("ChatBot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []


for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.text(message["content"])



user_input=st.chat_input("Type your message here...")
if user_input:
    st.session_state["messages"].append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.text(user_input)

    response=chatbot.invoke({"messages": [HumanMessage(content=user_input)]}, config=config1)
    ai_message=response['messages'][-1].content
    st.session_state["messages"].append({"role":"assistant","content":ai_message})
    with st.chat_message("assistant"):
        st.text(ai_message)