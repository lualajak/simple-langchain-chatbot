# simple-langchain-chatbot
================================================

A simple, local conversational chatbot built with LangChain and OpenAI. 
It remembers chat history, responds in real time, and runs fully on your machine using your own API key.

✨ Features
-----------
- 🤖 Uses LangChain’s ConversationChain
- 🧵 Maintains chat history with ConversationBufferMemory
- 🔐 Loads API keys from .env for security
- 🎯 Custom system prompt (you define the assistant's tone)
- 🔁 Runs in a loop until user exits

🧰 Tech Stack
-------------
- Python 3.10+
- LangChain
- OpenAI API
- python-dotenv

📦 Installation
---------------
git clone https://github.com/your-username/conversational-chatbot.git
cd conversational-chatbot
pip install -r requirements.txt

🔐 Setup Environment Variables
------------------------------
Create a .env file in the root folder with:

OPENAI_API_KEY=your-openai-api-key
OPENAI_BASE_URL=https://api.openai.com/v1

🚀 Run the Chatbot
------------------
python chatbot.py

The chatbot will keep responding until you type "quit" or "exit".

🧠 System Prompt
----------------
You can edit the chatbot’s behavior in the chatbot.py file by changing the system message. For example:

"You are called Sora, a helpful AI Assistant..."

🤝 Connect
----------
Like this project? Reach out or follow me on LinkedIn: https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile

#LangChain #OpenAI #Chatbot #Python #AI
