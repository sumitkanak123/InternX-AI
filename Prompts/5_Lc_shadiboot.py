from langchain_core.prompts import load_prompt
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv
import random

load_dotenv()

st.set_page_config(page_title="Match Maker", page_icon="💘")

# ---------- UI STYLE ----------

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

/* headings */

h1,h2,h3{
color:#ffd700;
text-align:center;
}

/* labels */

label{
color:white;
font-weight:bold;
}

/* button */

.stButton>button{
background:linear-gradient(45deg,#0072ff,#00c6ff);
color:white;
font-size:18px;
border-radius:10px;
padding:10px 25px;
}

/* romantic result box */

.result-box{
background: linear-gradient(135deg,#ff9a9e,#fad0c4);
padding:30px;
border-radius:25px;
color:#4a0033;
font-size:18px;
box-shadow:0px 0px 25px rgba(255,255,255,0.4);
animation: glow 2s infinite alternate;
}

@keyframes glow{
from{box-shadow:0 0 10px #ff99cc;}
to{box-shadow:0 0 25px #ff0066;}
}

</style>
""",unsafe_allow_html=True)

# ---------- LANGUAGE ----------

language = st.selectbox(
"🌐 Select Language",
["English","Hindi","Gujarati","Marathi","Punjabi"]
)

titles = {
"English":"💘 AI Match Maker",
"Hindi":"💖 जीवनसाथी खोजें",
"Gujarati":"💖 જીવનસાથી શોધો",
"Marathi":"💖 जीवनसाथी शोधा",
"Punjabi":"💖 ਜੀਵਨ ਸਾਥੀ ਲੱਭੋ"
}

st.title(titles[language])

# ---------- MODEL ----------

endpoint = HuggingFaceEndpoint(
repo_id="Qwen/Qwen2.5-1.5B-instruct",
task="text-generation",
max_new_tokens=400,
temperature=0.7
)

cm = ChatHuggingFace(llm=endpoint)

# ---------- FORM ----------

name = st.text_input("👤 Name")

gender = st.selectbox("⚧ Gender", ["Male","Female"])

age = st.number_input("🎂 Age",18,60)

height = st.text_input("📏 Height")

education = st.text_input("🎓 Education")

job = st.text_input("💼 Profession")

Religion = st.text_input("🕌 Religion")

location = st.text_input("📍 Location")

partner_preference = st.text_area("❤️ Partner Preference")

template = load_prompt("./sumit.json")

# ---------- BUTTON ----------

buttons = {
"English":"💞 Find My Match",
"Hindi":"💞 मेरा जीवनसाथी खोजें",
"Gujarati":"💞 મારું જીવનસાથી શોધો",
"Marathi":"💞 माझा जीवनसाथी शोधा",
"Punjabi":"💞 ਮੇਰਾ ਜੀਵਨ ਸਾਥੀ ਲੱਭੋ"
}

generate = st.button(buttons[language])

# ---------- RESULT ----------

if generate:

    chain = template | cm

    if all([
        name.strip(),
        height.strip(),
        education.strip(),
        job.strip(),
        Religion.strip(),
        location.strip(),
        partner_preference.strip()
    ]):

        with st.spinner("🔍 AI searching your destiny..."):

            result = chain.invoke({
                "name": name,
                "gender": gender,
                "age": age,
                "height": height,
                "education": education,
                "job": job,
                "Religion": Religion,
                "location": location,
                "partner_preference": partner_preference,
                "language": language
            })

            score=random.randint(70,98)

            personality=[
            "Romantic and caring 💕",
            "Little ziddi but loving 💖",
            "Calm and understanding 🌸",
            "Gusse wali but dil se soft ❤️",
            "Family loving and emotional 💞"
            ]

            marriage_type=[
            "Love Marriage ❤️",
            "Arranged Marriage 💍",
            "Love + Arranged 💑"
            ]

            partner_personality=random.choice(personality)

            marriage=random.choice(marriage_type)

            st.markdown(f"""
<div class="result-box">

💘 <b>Compatibility Score:</b> {score}%

🌸 <b>Partner Personality:</b> {partner_personality}

💑 <b>Marriage Possibility:</b> {marriage}

💖 <b>Partner Nature:</b> Caring • Loyal • Emotional

🌷 <b>Romantic Message:</b>

✨ Someone with a beautiful heart may soon enter your life.

<br><br>

{result.content}

</div>
""",unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please fill all details")
