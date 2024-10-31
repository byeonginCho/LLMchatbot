import cmd

class Chatbot(cmd.Cmd):
    prompt = "당신: "
    def default(self, line):
        response = model.generate_response(line)  # 모델을 통해 입력 받은 내용에 대한 응답을 생성
        print("챗봇:", response)

if __name__ == '__main__':
    Chatbot().cmdloop()