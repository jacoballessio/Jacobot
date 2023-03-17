import json
import os

class ChatbotMemory:
    def __init__(self, memory_file="chatbot_memory.json"):
        self.memory_file = memory_file
        self.chat_history = []

        # Load previous chat history if file exists
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as f:
                self.chat_history = json.load(f)

    def save_message(self, message):
        # Add message to chat history
        self.chat_history.append(message)

        # Save chat history to file
        with open(self.memory_file, "w") as f:
            json.dump(self.chat_history, f, indent=4)

    def get_chat_history(self):
        return self.chat_history

def main():
    chatbot_memory = ChatbotMemory()

    # Sample messages
    messages = [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "chatbot", "content": "Hi, I'm doing well! How about you?"},
        {"role": "user", "content": "I'm doing great, thank you!"},
        {"role": "chatbot", "content": "You're welcome! Let me know if you need any help."},
    ]

    for message in messages:
        chatbot_memory.save_message(message)

    print("Chat history:")
    for message in chatbot_memory.get_chat_history():
        print(f"{message['role'].capitalize()}: {message['content']}")

if __name__ == "__main__":
    main()
