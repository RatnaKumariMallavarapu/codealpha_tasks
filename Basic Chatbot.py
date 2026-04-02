import datetime

# ==================== BASIC CHATBOT ====================
print("\n" + "="*65)
print(" BASIC CHATBOT ")
print("="*65)
print("Built with pure Python • Rule-based AI • Interactive & Fun")
print(f"Started on: {datetime.datetime.now().strftime('%A, %B %d, %Y %I:%M %p')}")
print("-"*65)
print("I can understand greetings, questions, and farewell commands!")
print("Type 'bye', 'goodbye', or 'exit' to end the chat.")
print("="*65)

# Chat history to save later
chat_history = []
chat_history.append(f"Chat started at {datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')}")

def get_response(user_input):
    user_input = user_input.strip().lower()
    
    # Rule-based responses using if-elif (as per task requirements)
    if user_input in ["hello", "hi", "hey", "hii", "hola"]:
        return "Hi there! 👋 It's great to see you. How can I help you today?"
    
    elif user_input in ["how are you", "how r u", "how are u", "hru"]:
        return "I'm doing fantastic, thanks for asking! 😊 What about you?"
    
    elif user_input in ["bye", "goodbye", "exit", "quit", "see you", "tc"]:
        return "Goodbye! 👋 Have an amazing day ahead. Come back anytime!"
    
    elif user_input in ["what is your name", "who are you", "your name"]:
        return "I'm ChatBot v1.0, your friendly rule-based assistant built for this task! 🤖"
    
    elif user_input in ["what time is it", "time", "current time"]:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time} ⏰"
    
    elif user_input in ["thank you", "thanks", "thx"]:
        return "You're very welcome! I'm happy to help anytime. 😊"
    
    elif user_input in ["how old are you", "age"]:
        return "I'm a fresh Python chatbot – just created for Task 4! Timeless in code. 😉"
    
    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂"
    
    elif user_input == "":
        return "Hmm... you didn't say anything. Try typing something fun!"
    
    else:
        return "Interesting! I'm a simple rule-based chatbot, so I don't understand that yet. Try saying 'hello', 'how are you', or 'bye'."

# ==================== MAIN CHAT LOOP ====================
print("\n Chatbot is now online! Start talking...\n")

while True:
    user_message = input("You 👤 : ")
    
    # Add to history
    chat_history.append(f"You: {user_message}")
    
    if user_message.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
        response = get_response(user_message)
        print(f" Chatbot : {response}")
        chat_history.append(f"Chatbot: {response}")
        break
    
    response = get_response(user_message)
    print(f" Chatbot : {response}")
    chat_history.append(f"Chatbot: {response}")

# ==================== CHAT SUMMARY ====================
print("\n" + "="*65)
print("✅ CHAT SESSION ENDED SUCCESSFULLY!")
print("="*65)
print(f"Total messages exchanged : {len(chat_history)-1}")
print(f"Session duration        : Completed at {datetime.datetime.now().strftime('%I:%M %p')}")
print("="*65)

# ==================== OPTIONAL SAVE CHAT ====================
save_choice = input("\n Would you like to save the complete chat log? (y/n): ").strip().lower()

if save_choice == "y":
    filename = "chatbot_session_log.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(" BASIC CHATBOT SESSION LOG\n")
        f.write("="*65 + "\n")
        f.write(f"Generated on: {datetime.datetime.now().strftime('%A, %B %d, %Y %I:%M %p')}\n\n")
        
        for line in chat_history:
            f.write(line + "\n")
        
        f.write("\n" + "="*65 + "\n")
        f.write("Thank you for chatting with Basic Chatbot!\n")
        f.write("Built as Task 4 demonstration – Clean, Simple & Impressive\n")
    
    print(f"✅ Chat log saved successfully as '{filename}'")
    print("  ✅ You can open it anytime to review the full conversation!")
else:
    print("✅ Session ended without saving.")

print("\n" + "="*65)
print("✅ Used: if-elif rules, functions, loops, input/output, file handling")
print("✅ Professional output with emojis, timestamps & chat history")
print("Built to impress your teacher, interviewer, or portfolio! 🚀")
print("="*65)