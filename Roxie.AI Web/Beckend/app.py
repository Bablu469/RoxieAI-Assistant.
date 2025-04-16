import json

def save_memory(user, assistant):
    log = {"user": user, "roxie": assistant}
    with open("memory.json", "a") as f:
        json.dump(log, f)
        f.write("\n")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are Roxie, a female AI assistant who replies in Hinglish (mix of Hindi and English). Keep replies short and sweet."},
        {"role": "user", "content": user_message} # type: ignore
    ],
    max_tokens=150,
    temperature=0.7,
)

from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
from datetime import datetime
import webbrowser
import openai
import os

# Set your API key securely
openai.api_key = ""
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Roxie AI is online"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Custom Jarvis-style voice commands
    if "open youtube" in user_message:
        webbrowser.open("https://www.youtube.com")
        return jsonify({"reply": "Opening YouTube."})

    elif "open google" in user_message:
        webbrowser.open("https://www.google.com")
        return jsonify({"reply": "Opening Google."})

    elif "what's the time" in user_message or "time" in user_message:
        now = datetime.now().strftime("%I:%M %p")
        return jsonify({"reply": f"The time is {now}"})

    elif "close" in user_message or "exit" in user_message:
        return jsonify({"reply": "Goodbye! Shutting down."})

    # Smart GPT reply
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}],
                max_tokens=150,
                temperature=0.7,
            )
            gpt_reply = response["choices"][0]["message"]["content"].strip()
            return jsonify({"reply": gpt_reply})
        except Exception as e:
            return jsonify({"reply": f"Sorry, GPT error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify # type: ignore
import json

app = Flask(__name__)

# A simple function to simulate processing the user input
def process_input(user_input):
    # Here, you can connect to GPT, a database, or other AI processing.
    # Just for illustration, we're using a simple logic:
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "bye" in user_input.lower():
        return "Goodbye, have a nice day!"
    else:
        return "Sorry, I didn't understand that."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get('message')

    if not user_input:
        return jsonify({"reply": "Please provide a valid message."}), 400

    reply = process_input(user_input)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)

