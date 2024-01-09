import requests


def chat_api(messages, params=None):
    url = "http://localhost:19327/v1/chat/completions"
    headers = {"Content-Type": "application/json"}

    data = {"messages": messages}

    if params:
        data.update(params)

    response = requests.post(url, headers=headers, json=data)
    return response.json()


def main():
    conversation = []

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        message = {"role": "user", "content": user_input}
        conversation.append(message)

        # Set advanced parameters as needed
        advanced_params = {
            "temperature": 0.8,
            "max_tokens": 500,
            "num_beams": 5,
            "top_k": 50,
            "top_p": 0.9,
            "repetition_penalty": 1.2,
            "do_sample": True,
            "stream": False
        }

        response = chat_api(conversation, params=advanced_params)
        assistant_reply = response["choices"][-1]["message"]["content"]

        print(f"Assistant: {assistant_reply}")
        conversation.append({"role": "assistant", "content": assistant_reply})


if __name__ == "__main__":
    main()
