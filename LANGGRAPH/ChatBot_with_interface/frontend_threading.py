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


    with st.chat_message("assistant"):
        ai_message=st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=config1,
                stream_mode="messages"
            )
        ) 
    st.session_state["messages"].append({"role":"assistant","content":ai_message})
    