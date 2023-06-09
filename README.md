# Jacobot
Jacobot a helpful personalized chatbot powered by GPT-4. The goal is to create an easily accessible telegram chatbot that takes advantage of the major advancements in LLM technology. A subgoal of the project is to make make it more interfacable with groups (For example, in a groupchat the chatbot shouldn't respond to every message; only ones addressed to it or where it could be helpful). This project also implements a custom memory system that creates a summary of each conversation and stores it in a JSON file. However, this method is only able to remember the general idea of things, and nearly doubles the token cost. The plan is to eventually switch this memory system out with a vector database such as pinecone.

Installation instructions: 
1. Run the "requirements.txt file
```pip install -r requirements.txt```

2. Add your telegram bot token to the "telegram_token.txt" file, and your OpenAI API key to the "openai_key.txt" file.

3. Run Jacobot python file
```python Jacobot4/main.py```
4. Finally, test that your telegram bot works (you may need to send /start to it first)

Note: GPT-3.5 module is broken currently. Will be fixing in future update.

# Example interaction with Jacobot:
![Capture](https://github.com/jacoballessio/Jacobot/assets/39074704/48eb0fc1-47c9-4b63-8d80-704ebf7e142f)
