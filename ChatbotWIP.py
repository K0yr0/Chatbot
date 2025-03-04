
import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem.",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by OpenAI. You can call me Chatbot.",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
    [
        r"(.*)",
        ["I am not sure how to respond to that. Could you please rephrase?",]
    ],
]

chatbot = Chat(pairs, reflections)

def send_message():
    user_message = user_input.get()
    if user_message.strip() == "":
        return 
    
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_message}\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END) 
    user_input.delete(0, tk.END)
    
    bot_response = chatbot.respond(user_message)
    
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"Bot: {bot_response}\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END) 

root = tk.Tk()
root.title("Chatbot")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, state='disabled')
chat_area.pack(pady=10)

user_input = tk.Entry(root, width=50)
user_input.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.bind('<Return>', lambda event: send_message())

root.mainloop()