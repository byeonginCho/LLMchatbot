import tkinter as tk

def show_message():
    # 입력된 메시지 가져오기
    user_input = entry.get()
    
    # Label을 업데이트하여 메시지 표시
    label.config(text="입력 받은 메시지: " + user_input)
    
    # 입력 필드 초기화
    entry.delete(0, tk.END)

# 기본 창 생성
root = tk.Tk()
root.title("메시지 입력 및 출력")

# 입력 필드
entry = tk.Entry(root, width=50)
entry.pack(pady=20)

# 버튼 추가
button = tk.Button(root, text="메시지 보여주기", command=show_message)
button.pack(pady=10)

# 메시지를 보여줄 레이블
label = tk.Label(root, text="여기에 입력한 메시지가 표시됩니다.", height=4)
label.pack(pady=20)

# 창 실행
root.mainloop()
