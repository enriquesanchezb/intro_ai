import json
import requests

MODEL = "mistral"


def chat(messages):
    r = requests.post(
        "http://0.0.0.0:11434/api/chat",
        json={"model": MODEL, "messages": messages, "stream": True},
        timeout=10,
    )
    r.raise_for_status()
    output = ""

    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise ValueError(body["error"])
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content
            # the response streams one token at a time, print that as we receive it
            print(content, end="", flush=True)

        if body.get("done", False):
            message["content"] = output
            return message


def main():
    messages = []

    while True:
        user_input = input(">> Enter a prompt: ")
        if not user_input:
            exit()
        print()
        messages.append({"role": "user", "content": user_input})
        message = chat(messages)
        messages.append(message)
        print("\n\n")


if __name__ == "__main__":
    main()
