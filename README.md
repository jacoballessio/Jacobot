# Jacobot
Jacobot a helpful personalized bot powered by GPT-4. The goal is to create an easily accessible telegram chatbot that takes advantage of the major advancements in LLM technology. A subgoal of the project is to make make it more interfacable with groups (For example, in a groupchat the chatbot shouldn't respond to every message; only ones addressed to it or where it could be helpful). This project also implements a custom memory system that creates a summary of each conversation and stores it in a JSON file. However, this method is only able to remember the general idea of things, and nearly doubles the token cost. The plan is to eventually switch this memory system out with a vector database such as pinecone.

Installation instructions: 
1. Run the "requirements.txt file
```pip install -r requirements.txt```

2. Add your telegram bot token to the "telegram_token.txt" file, and your OpenAI API key to the "openai_key.txt" file.

3. Run jacobot.py for GPT-3
```python jacobot.py```
or ""
4. Finally, test that your telegram bot works (you may need to send /start to it first)
