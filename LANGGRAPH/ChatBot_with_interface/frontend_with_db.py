import streamlit as st
from backend_with_tools import chatbot
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import uuid
from backend_db import retrieve_all_threads

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
def load_convo(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    values = getattr(state, 'values', {}) or {}
    return values.get('messages', [])

st.title("ChatBot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

st.sidebar.title("LangGraph ChatBot")

if st.sidebar.button('new chat'):
    reset_chat()

st.sidebar.header('My conversations')

for thread_id in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        message= load_convo(thread_id)

        temp_messages=[]
        for msg in message:
            if isinstance(msg,HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({"role":role,"content":msg.content})
        st.session_state["messages"] = temp_messages



for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])



user_input=st.chat_input("Type your message here...")
if user_input:
    st.session_state["messages"].append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.text(user_input)

    Config={
        'configurable':{'thread_id':st.session_state['thread_id']},
        "metadata":{
            "thread_id":st.session_state['thread_id']
        },
        "run_name":"chat_run"
    }

    with st.chat_message("assistant"):
        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=Config,
                stream_mode="messages"
            ):
                if isinstance(message_chunk, AIMessage):
                    # yield only assistant tokens
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

    st.session_state['messages'].append({
        'role': 'assistant',
        'content': ai_message
    })
    