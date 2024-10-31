from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "beomi/Llama-3-Open-Ko-8B-Instruct-preview"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "system", "content": "친절한 챗봇으로서 상대방의 요청에 최대한 자세하고 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘."},
    {"role": "user", "content": "넌 모델이름이 뭐야??"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
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
print(tokenizer.decode(response, skip_special_tokens=True))


# modular

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
prompt = [
    {"role": "system", "content": "친절한 챗봇으로서 상대방의 요청에 최대한 자세하고 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘. 예외로 학문적인 맥락에서 용어 대용(Loanword substitution)은 그 단어만 영어로 표시해줘"},
    {"role": "user", "content": "코딩하다가 _tkinter를 사용하는 투명한 창을 만들고 싶어 transparent가 아닌가?"}
]

response_text = generate_text(prompt)
print(response_text)
