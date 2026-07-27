from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_template=ChatPromptTemplate([
    ('system',"you are a helpful customer suport agent"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history=[]
with open('message.txt') as f:
    chat_history.append(f.readlines())
print(chat_history)

prompt=chat_template.invoke({'chat_history':chat_history,'query':'where is mt refund'})
print(prompt)