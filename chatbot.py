# --- Import Required Libraries ---
import nltk
import random
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data (only once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# --- Knowledge Base: Predefined Topics and Responses ---
knowledge_base = {
    "variables": "In Python, variables are used to store data values. You can assign a value using '='. Example: x = 5.",
    "datatypes": "Python supports various data types like int, float, string, list, tuple, dict, and set.",
    "loops": "Python has 'for' and 'while' loops. Example: for i in range(5): print(i)",
    "functions": "Functions are defined using the 'def' keyword. Example: def greet(): print('Hello!')",
    "conditions": "Conditional statements include if, elif, and else. Example: if x > 0: print('Positive')",
    "lists": "Lists are ordered, mutable collections. Example: my_list = [1, 2, 3]",
    "strings": "Strings are sequences of characters enclosed in quotes. Example: name = 'Priya'",
    "exceptions": "Exceptions handle runtime errors. Example: try: x=1/0 except ZeroDivisionError: print('Error!')",
    "filehandling": "File handling is done using open(), read(), write(), and close(). Example: f=open('file.txt','r')",
    "oop": "Python supports Object-Oriented Programming with classes and objects. Example: class Student: pass"
}

# --- NLP Preprocessing Function ---
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# --- Response Generator ---
def generate_response(user_input):
    tokens = preprocess(user_input)
    for key, answer in knowledge_base.items():
        if key in tokens:
            return answer
    
    # Keyword-based fallback detection
    if any(re.search(r'\bhi+\b|\bhey+\b|\bhello+\b', word) for word in tokens):
        return "Hello! I'm your Python Learning Assistant. What would you like to learn today?"
    elif "help" in tokens or "learn" in tokens:
        return "Sure! You can ask me about Python topics like variables, loops, functions, or OOP."
    elif "thanks" in tokens or "thank" in tokens:
        return "You're welcome! 😊 Keep learning Python."
    elif "bye" in tokens or "exit" in tokens:
        return "Goodbye! Keep coding and exploring Python! 👋"
    else:
        return "Hmm, I’m not sure about that yet. Try asking about Python basics like loops, variables, or functions."

# --- Chatbot Loop ---
print("🤖 PyTutor: Your Python Learning Chatbot is Online!")
print("Type 'bye' or 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("PyTutor: Goodbye! Keep coding and exploring Python! 👋")
        break
    response = generate_response(user_input)
    print("PyTutor:", response)
