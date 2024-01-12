from langchain_community.llms import Ollama

ollama = Ollama(model="mistral")


def chat(messages):
    return ollama.invoke(messages)


def main():
    while True:
        user_input = input(">> Enter a prompt: ")
        if not user_input:
            exit()
        print(chat(user_input))
        print("\n\n")


if __name__ == "__main__":
    main()
