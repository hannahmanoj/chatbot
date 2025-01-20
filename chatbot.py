import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords
import nltk
nltk.download("stopwords")
nltk.download("punkt")

responses = {
    "name": "I am a chatbot!",
    "help": "I can answer simple questions.",
    "weather": "I don't have weather data now, but I'm learning!",
    "default": "I'm sorry, I don't understand that question.",
    "joke": "Why did the computer cross the road? To get to the other side!"
}

def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    return [word for word in words if word.isalnum() and word not in stop_words]

def chatbot_response(user_input):
    processed_input = preprocess_text(user_input)
    for key in responses:
        if key in processed_input:
            return responses[key]
    return responses["default"]

def chat():
    user_name=input("Chatbot: What's your name? -> ")
    print("Hey, ",user_name, "! Ask me anything (enter 'exit' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    chat()

