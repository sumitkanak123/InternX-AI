from langchain_core.prompts import load_prompt
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
endpoint=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-instruct",
    task="text-generation"
)
cm=ChatHuggingFace(llm=endpoint)
st.header("AI Relationship Assistant")

# INPUTS
name = st.text_input("Name")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 18, 60)
education = st.text_input("Education")
job = st.text_input("Profession / Job")
Religion = st.text_input("Religion")
location = st.text_input("Village / City / State")
family = st.text_area("Family Details")
partner_preference = st.text_area("Partner Preference")

template = load_prompt("./sumit.json")

#GENERATE BUTTON
if st.button("Find Match / Generate Profile"):
    chain=template |cm
    if all([
        name.strip(),
        education.strip(),
        job.strip(),
        Religion.strip(),
        location.strip(),
        family.strip(),
        partner_preference.strip()
    ]):

        with st.spinner("Searching suitable match..."):

            result = chain.invoke({
                "name": name,
                "gender": gender,
                "age": age,
                "education": education,
                "job": job,
                "Religion": Religion,
                "location": location,
                "family": family,
                "partner_preference": partner_preference
            })

            st.subheader("AI Relationship Generate")
            st.write(result.content)

    else:
        st.warning("Please fill all details")