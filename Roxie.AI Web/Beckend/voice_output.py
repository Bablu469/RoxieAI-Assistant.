from gtts import gTTS
import playsound
import os
import uuid

def speak(text):
    print(f"🗣️ Roxie says: {text}")
    
    try:
        # Save unique filename to avoid conflicts
        filename = f"voice_{uuid.uuid4()}.mp3"
        tts = gTTS(text=text, lang='hi', slow=False)  # Use 'hi' for Hindi + Hinglish

        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    except Exception as e:
        print("❌ Error in TTS:", e)

# voice_output.py

from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")  # This works on Windows; for macOS, use "open output.mp3"
