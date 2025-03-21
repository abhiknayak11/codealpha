import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Predefined responses for chatbot patterns
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! How can I assist you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Goodbye! Take care!"],
    "thanks": ["You're welcome!", "Happy to help!", "No problem!"],
    "how_are_you": ["I'm just a bot, but I'm doing great! How about you?", "I'm doing well, thank you for asking!", "I'm functioning as expected! How are you?"],
    "default": ["Sorry, I don't understand that.", "Can you rephrase?", "I'm not sure how to respond to that."]
}

# Function to preprocess user input: tokenize, lowercase, remove stopwords, etc.
def preprocess_input(user_input):
    # Tokenizing the input sentence
    tokens = word_tokenize(user_input.lower())
    
    # Remove stopwords (common words like 'the', 'and', etc.)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    
    return filtered_tokens

# Function to generate response based on user input
def get_response(user_input):
    tokens = preprocess_input(user_input)
    
    # Basic pattern matching for predefined categories
    if any(word in tokens for word in ["hello", "hi", "hey", "greetings"]):
        return random.choice(responses["greeting"])
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return random.choice(responses["goodbye"])
    elif any(word in tokens for word in ["thanks", "thank", "grateful"]):
        return random.choice(responses["thanks"])
    elif any(word in tokens for word in ["how", "are", "you"]):
        return random.choice(responses["how_are_you"])
    else:
        return random.choice(responses["default"])

# Main function to start the chatbot
def start_chatbot():
    print("Hello! I am your friendly chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition for the chat
        if user_input.lower() == "exit":
            print("Goodbye! Take care!")
            break
        
        # Get the chatbot's response
        response = get_response(user_input)
        
        print("Chatbot:", response)

# Start the chatbot
if __name__ == "__main__":
    start_chatbot()
