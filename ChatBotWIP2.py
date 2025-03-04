import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Load the text-generation model (GPT-2)
generator = pipeline("text-generation", model="gpt2")

# Store conversation history
conversation_history = []

# Function to generate chatbot response
def chat_with_bot(user_input):
    global conversation_history

    # Append user input to conversation history
    conversation_history.append(f"You: {user_input}")

    # Keep conversation context short (last few exchanges)
    chat_context = " ".join(conversation_history[-5:])

    try:
        # Generate response using GPT-2
        bot_response = generator(chat_context, max_new_tokens=50, pad_token_id=50256)[0]['generated_text']

        # Extract only new bot response (avoid repeating history)
        bot_response = bot_response[len(chat_context):].strip().split("\n")[0]

        # Store bot's response in history
        conversation_history.append(f"Bot: {bot_response}")

        return bot_response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Oops! Something went wrong. Please try again."

# Create GUI window
root = tk.Tk()
root.title("AI Chatbot")

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, state='disabled')
chat_area.pack(pady=10)

# User input field
user_input = tk.Entry(root, width=50)
user_input.pack(pady=10)

# Function to handle message sending
def send_message(event=None):
    user_message = user_input.get().strip()
    if not user_message:
        return  # Ignore empty input
    
    # Display user's message
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_message}\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    user_input.delete(0, tk.END)

    # Get chatbot response
    bot_response = chat_with_bot(user_message)

    # Display bot's response
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"Bot: {bot_response}\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Bind Enter key to send message
root.bind('<Return>', send_message)

# Start the chatbot GUI
root.mainloop()
