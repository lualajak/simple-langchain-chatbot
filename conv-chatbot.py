import os
from dotenv import load_dotenv
from langchain.chains.conversation.base import ConversationChain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain.memory import ConversationBufferMemory

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

system_prompt = SystemMessage(
    content="""You are called Sora, an AI Assistant, You Task to assist the 
    user in a professional Manner, Pricise and Clear"""
)

memory = ConversationBufferMemory(return_messages=True)

prompt = ChatPromptTemplate.from_messages([
    system_prompt,
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

while True:
    user_input = input("You: ")
    if  user_input.lower() in ["quit", "exit"]:
        print("Good-Bye")
        break
    response = conversation.predict(input=user_input)
    print("Bot: ", response)