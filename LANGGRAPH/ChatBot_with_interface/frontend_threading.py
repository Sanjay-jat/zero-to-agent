import streamlit as st
from backend import chatbot
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import uuid


def generate_thread_id():
    thread_id=uuid.uuid4()
    return thread_id
def reset_chat():
    st.session_state['thread_id'] = generate_thread_id()
    add_thread_id(st.session_state['thread_id'])
    st.session_state["messages"] = []
def add_thread_id(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)
    
st.title("ChatBot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

st.sidebar.title("LangGraph ChatBot")

if st.sidebar.button('new chat'):
    reset_chat()

st.sidebar.header('My conversations')

for thread_id in st.session_state['chat_threads']:
    st.sidebar.text(thread_id)








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
                config={'configurable':{'thread_id':st.session_state['thread_id']}},
                stream_mode="messages"
            )
        ) 
    st.session_state["messages"].append({"role":"assistant","content":ai_message})
    