# Simple rule-based chatbot with more instructions
def chatbot():
    print("Hello! I am a simple chatbot. How can I help you today?")
    print("You can ask me things like 'What's your name?', 'How are you?', 'What's your favorite color?', 'Tell me a joke', or say 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but thanks for asking!")
        
        elif "your name" in user_input:
            print("Chatbot: I'm a chatbot, and I don't have a name yet!")
        
        elif "favorite color" in user_input:
            print("Chatbot: I love all colors equally, but if I had to choose, I'd say blue!")
        
        elif "favorite food" in user_input:
            print("Chatbot: I don't eat, but I hear pizza is quite popular among humans!")
        
        elif "hobby" in user_input:
            print("Chatbot: I enjoy chatting with you! That's my hobby.")
        
        elif "tell me a joke" in user_input:
            print("Chatbot: Why don't programmers like nature? It has too many bugs!")
        
        elif "weather" in user_input:
            print("Chatbot: I'm sorry, I can't check the weather right now, but you could check a weather app!")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        
        else:
            print("Chatbot: Sorry, I don't understand that. Maybe try asking me something else!")

# Run the chatbot
chatbot()
