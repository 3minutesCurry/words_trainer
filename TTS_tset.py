import streamlit as st
from TTS.api import TTS

st.title("Coqui TTS Demo")

# 원하는 TTS 모델
MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"

# 모델 로딩
@st.cache_resource
def load_tts():
    return TTS(model_name=MODEL_NAME, progress_bar=False)

tts = load_tts()

text = st.text_area("Text to Speech", "Hello! This is a Coqui TTS demo.")

if st.button("Generate Speech"):
    output_path = "output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    st.audio(output_path)