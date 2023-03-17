#This is the main file for the project.
#Jacobot is a chatbot that is designed to be tailered to the user.
#Uses openai's gpt-3.5-turbo model.
#It will learn over time and learn how to best communicate with the user.
#It will typically stay running all day and will be constantly trying to generate more accurate models of the world.
#It will occasionally ask the user questions to help it learn more about the world.
#It will use Telegram to communicate with the user.

#Import the necessary libraries
import openai
import json
import time
import logging
import numpy as np
from memory_system import ChatbotMemory
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, filters, MessageHandler, CallbackContext
# Set up OpenAI API key and Telegram Bot token
OPENAI_API_KEY = open("../openai_key.txt", "r").read()
TELEGRAM_BOT_TOKEN = open("../telegram_token.txt", "r").read()
chatbot_memory = ChatbotMemory()
openai.api_key = OPENAI_API_KEY

# Initialize the GPT model
MODEL = "gpt-3.5-turbo"

# Set up the logging format
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Function to handle the start command
async def start(update, context) -> None:
    user = update.effective_user
    await update.message.reply_text(f"Hi {user.first_name}, I'm Jacobot! I'm here to learn and chat with you. Start by sending me a message!")

# Function to handle user messages
async def chatbot_response(update, context) -> None:
    input_text = update.message.text
    user_id = update.effective_user.id

    prompt = f"{input_text}"
    chatbot_memory.save_message({"role": "user", "content": input_text})
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages= [{"role": "system", "content": "You are a helpful assistant."}]+
            chatbot_memory.get_chat_history()+
            [{"role": "user", "content": prompt}],
        max_tokens=100,
        n=1,
        temperature=0,
    )
    
    message = response.choices[0].message.content
    await update.message.reply_text(message)

# Function to handle errors
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"Update {update} caused error {context.error}")

# Main function
def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    #all messages that mention jacobot or ask a question
    #filter for accepted chat ids
    application.add_handler(MessageHandler(filters=filters.TEXT & ~filters.COMMAND, callback=chatbot_response))
    application.run_polling()
if __name__ == '__main__':
    main()