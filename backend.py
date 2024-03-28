from openai import OpenAI


# Replace with your ChatGPT API key
client = OpenAI(
    # This is the default and can be omitted
    api_key="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"
)


def agrichatbot(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = agrichatbot(user_input)
        print("Chatbot: ", response)