import streamlit as st
from gtts import gTTS
import os

# Supported languages for the dropdown (a few examples including Malayalam)
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Hindi": "hi",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
    "Malayalam": "ml"  # Added Malayalam
}

# Streamlit page setup
st.title("Text-to-Speech Converter ")
st.write("Type something and hear it spoken in different languages!")

# Text input area
text_input = st.text_area("Enter Text", "Welcome to the Text-to-Speech converter demo for kids.", height=150)

# Language selection dropdown
lang_selection = st.selectbox("Select Language", list(LANGUAGES.keys()))

# Button to trigger text-to-speech conversion
if st.button("Convert to Speech"):
    if text_input.strip():  # Ensure the text input is not empty
        # Get the language code from the selection
        lang_code = LANGUAGES[lang_selection]
        
        # Convert text to speech using gTTS
        tts = gTTS(text=text_input, lang=lang_code, slow=False)
        
        # Save the speech to an MP3 file
        tts.save("output.mp3")
        
        # Play the audio file in Streamlit
        with open("output.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        
        # Download option for the generated MP3 file
        st.download_button(label="Download Speech", data=audio_bytes, file_name="output.mp3", mime="audio/mp3")
    else:
        st.warning("Please enter some text to convert.")
