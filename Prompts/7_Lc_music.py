from langchain_core.prompts import load_prompt
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-instruct",
    task="text-generation"
)

cm = ChatHuggingFace(llm=endpoint)

st.header("🎧 AI Mood Based Song Recommender")

feeling = st.selectbox(
    "Select Your Mood",
    ["Sad 😔", "Happy 😊", "Angry 😡", "Romantic ❤️", "Focus 📚", "Tired 😴"]
)

language = st.selectbox(
    "Select Language",
    ["Hindi", "English", "Punjabi"]
)

# ✅ SAFE FILE PATH FIX
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "music_prompt.json")

template = load_prompt(file_path)

if st.button("Recommend Song"):

    chain = template | cm

    with st.spinner("Finding best song for you..."):

        result = chain.invoke({
            "feeling": feeling,
            "language": language
        })

        st.subheader("🎵 Recommended Song")
        st.write(result.content)
    