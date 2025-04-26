import streamlit as st
import speech_recognition as sr
import pyttsx3
import tempfile
import os

# Text-to-Speech
def speak_text(command):
    engine = pyttsx3.init()
    engine.save_to_file(command, "output.mp3")
    engine.runAndWait()
    return "output.mp3"

# Speech-to-Text
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

# Streamlit UI
st.title("🎙️ Speech-to-Text and Text-to-Speech")

if st.button("Start Listening"):
    result = recognize_speech()
    st.success(f"You said: {result}")
    
    # Speak back
    audio_file = speak_text(result)
    st.audio(audio_file, format='audio/mp3')
    os.remove(audio_file)
