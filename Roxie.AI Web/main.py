
from voice_output import speak
import requests

while True:
    user_input = input("You: ")

    if "exit" in user_input.lower():
        speak("Goodbye, sir. Main hamesha yahin hoon.")
        break

    # Send to GPT backend
    response = requests.post("http://127.0.0.1:5000/ask", json={"message": user_input})
    reply = response.json().get("reply")

    speak(reply)
    
    
import subprocess
import webbrowser
import threading
from time import sleep

def run_server():
    subprocess.call(["python", "Beckend/app.py"])

# Start Flask server in background thread
threading.Thread(target=run_server).start()

# Wait for server to start
sleep(2)

# Open front-end in browser
webbrowser.open("d:\Documents\Desktop\Roxie.AI Web")

from voice_output import speak
import requests
import subprocess
import webbrowser
import threading
from time import sleep
import os

def run_server():
    """Function to run the Flask server in the background."""
    subprocess.call(["python", "Beckend/app.py"])

def open_frontend():
    """Open the frontend web page in the default browser."""
    frontend_path = "file:///d:/Documents/Desktop/Roxie.AI Web/index.html"
    webbrowser.open(frontend_path)

def chat_with_assistant(user_input):
    """Function to interact with the assistant."""
    try:
        # Send user input to Flask backend
        response = requests.post("http://127.0.0.1:5000/ask", json={"message": user_input})
        if response.status_code == 200:
            reply = response.json().get("reply")
            return reply
        else:
            return "There was an error with the server. Please try again later."
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to connect to the server. {e}"

def run_assistant():
    """Main function to run the voice assistant."""
    while True:
        user_input = input("You: ")

        if "exit" in user_input.lower():
            speak("Goodbye, sir. Main hamesha yahin hoon.")
            break

        # Get the assistant's reply
        assistant_reply = chat_with_assistant(user_input)

        # Speak out the assistant's reply
        speak(assistant_reply)

def main():
    """Run the server and open frontend in a separate thread."""
    threading.Thread(target=run_server).start()

    # Wait for server to start
    sleep(2)

    # Open the frontend page
    open_frontend()

    # Start the assistant interaction loop
    run_assistant()

if __name__ == "__main__":
    main()
