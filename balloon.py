import tkinter as tk

class ChatInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat Interface")
        self.geometry("400x600")  # 창 크기 설정

        self.chat_frame = tk.Frame(self, bg='white')
        self.chat_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.text_box = tk.Text(self.chat_frame, height=2)
        self.text_box.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.send_button = tk.Button(self.chat_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.BOTTOM, pady=10)

        self.chat_log = tk.Text(self.chat_frame, state='disabled')
        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def send_message(self):
        user_input = self.text_box.get("1.0", tk.END).strip()
        if user_input:
            self.text_box.delete("1.0", tk.END)
            self.display_message("You: " + user_input)
            self.display_message("Bot: " + "Here is your response!")  # 임시 응답

    def display_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + '\n')
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

if __name__ == "__main__":
    app = ChatInterface()
    app.mainloop()
