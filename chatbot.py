from flask import Flask, request, jsonify, render_template
from openai import OpenAI

client = OpenAI(
api_key = "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"
)

app = Flask(__name__, template_folder='')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat_with_openai():
    # Get the message from the POST request
    print(request.json)
    data = request.json
    message = data['message']

    # Call the OpenAI API
    response = client.chat.completions.create(
 model="gpt-3.5-turbo",
messages=[{"role": "user", "content": message}]
    )

  # Return the response from OpenAI API
    return response.choices[0].message.content

if __name__=='__main__':
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
    )

  # Return the response from OpenAI API
    app.run(debug=True)