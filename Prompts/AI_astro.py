import streamlit as st
from langchain_core.prompts import load_prompt
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
import random
from datetime import date

load_dotenv()

st.set_page_config(page_title="AI Destiny Reader", layout="centered")

# ---------------- MAGIC CSS ---------------- #

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
}

/* Make ALL text white */
html, body, [class*="css"]  {
    color: #ffffff !important;
}

/* Labels */
label {
    color: #FFD700 !important;
    font-weight: bold;
}

/* Title Glow */
.magic-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #FFD700;
    text-shadow: 0px 0px 15px #ffcc00;
}

/* Button */
div.stButton > button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 15px;
    height: 3em;
    width: 100%;
    border: none;
    box-shadow: 0px 0px 15px rgba(255, 81, 47, 0.8);
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #f7971e, #ffd200);
    transform: scale(1.05);
}

/* Expander text */
.streamlit-expanderHeader {
    color: #FFD700 !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='magic-title'>🔮 AI Future Partner Predictor</div>", unsafe_allow_html=True)
st.write("Enter your details to reveal your cosmic destiny... ✨")

# ---------------- LLM ---------------- #

endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-instruct",
    task="text-generation"
)

cm = ChatHuggingFace(llm=endpoint)

# ---------------- Inputs ---------------- #

name = st.text_input("Your Name")
age = st.number_input("Your Age", min_value=18, max_value=60, step=1)

gender = st.selectbox("Gender", ["Male", "Female"])

dob = st.date_input(
    "Date of Birth",
    min_value=date(1990, 1, 1),
    max_value=date.today()
)

religion = st.selectbox(
    "Religion",
    ["Hindu", "Muslim", "Christian", "Sikh", "Other"]
)

country = st.selectbox(
    "Country",
    ["India", "USA", "UK", "Canada", "Other"]
)

state = st.text_input("State (Example: Uttar Pradesh)")

# 🔥 NEW LANGUAGE OPTION
language = st.selectbox(
    "Select Output Language",
    ["English", "Hindi"]
)

# ---------------- Prompt ---------------- #

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "astro_prompt.json")

try:
    template = load_prompt(file_path)
except Exception as e:
    st.error(f"Prompt Load Error: {e}")
    st.stop()

# ---------------- Button ---------------- #

if st.button("✨ Reveal My Destiny ✨"):

    if name == "" or state == "":
        st.warning("Please fill all required fields.")
    else:

        chain = template | cm

        with st.spinner("Consulting the stars... 🔮"):

            result = chain.invoke({
                "name": name,
                "dob": str(dob),
                "religion": religion,
                "age": age,
                "gender": gender,
                "country": country,
                "state": state,
                "language": language
            })

            love = random.randint(75, 95)
            emotional = random.randint(70, 98)
            finance = random.randint(65, 90)

            st.success("✨ Destiny Revealed ✨")

            st.markdown("### 💍 Future Partner Details")
            st.write(result.content)

            st.markdown("### 🌟 Compatibility Scores")
            st.metric("Love", f"{love}%")
            st.metric("Emotional", f"{emotional}%")
            st.metric("Financial", f"{finance}%")

st.caption("⚠ This AI prediction is for entertainment purposes only.")