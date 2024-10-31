from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "beomi/Llama-3-Open-Ko-8B-Instruct-preview"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

def generate_text(prompt, tokenizer=tokenizer, model=model):

    input_ids = tokenizer.apply_chat_template(
        prompt,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = model.generate(
        input_ids,
        max_new_tokens=512,
        eos_token_id=terminators,
        do_sample=True,
        temperature=1,
        top_p=0.9,
    )
    response = outputs[0][input_ids.shape[-1]:]
    return tokenizer.decode(response, skip_special_tokens=True)

# 예제 사용
"""
prompt = [
    {"role": "system", "content": "친절한 챗봇으로서 상대방의 요청에 최대한 자세하고 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘. 예외로 학문적인 맥락에서 용어 대용(Loanword substitution)은 그 단어만 영어로 표시해줘"},
    {"role": "user", "content": user_input }
]

response_text = generate_text(prompt)
print(response_text)
"""


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
            prompt = [{"role": "system", "content": "친절한 챗봇으로서 상대방의 요청에 최대한 자세하고 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘. 예외로 학문적인 맥락에서 용어 대용(Loanword substitution)은 그 단어만 영어로 표시해줘"},{"role": "user", "content": user_input }]
            response_text = generate_text(prompt)
            self.display_message("You: " + user_input)
            self.display_message("Bot: " + response_text)  # 임시 응답

    def display_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + '\n')
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

if __name__ == "__main__":
    app = ChatInterface()
    app.mainloop()
