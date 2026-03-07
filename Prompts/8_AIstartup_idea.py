import streamlit as st
import random
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Startup Name Generator", layout="centered")

st.title("🚀 AI Startup Name + Tagline Generator")

# ----------- Inputs ------------ #

industry = st.text_input("Industry (Example: AI, Finance, EdTech)")

audience = st.text_input("Target Audience (Example: Students, Businesses, Gen Z)")

vibe = st.selectbox(
    "Select Brand Vibe",
    ["Premium", "Playful", "Bold"]
)

# ----------- LLM Setup ------------ #

endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-instruct",
    task="text-generation"
)

llm = ChatHuggingFace(llm=endpoint)

prompt = PromptTemplate(
    input_variables=["industry", "audience", "vibe"],
    template="""
Generate 5 creative startup names for a {industry} company.
Target audience: {audience}
Brand vibe: {vibe}

For each name:
- Provide a short catchy tagline (max 8 words).
Keep response clean and structured.
"""
)

chain = prompt | llm

# ----------- Button ------------ #

if st.button("Generate Startup Ideas ✨"):

    if industry == "" or audience == "":
        st.warning("Please fill all fields.")
    else:
        with st.spinner("Generating creative ideas..."):

            result = chain.invoke({
                "industry": industry,
                "audience": audience,
                "vibe": vibe
            })

            st.success("🔥 Here Are Your Startup Ideas")

            st.markdown(result.content)

            # ----------- Mock Domain Checker ------------ #

            st.markdown("### 🌐 Domain Availability (Mock Check)")

            lines = result.content.split("\n")
            for line in lines:
                if line.strip() != "":
                    domain_status = random.choice(["Available ✅", "Taken ❌"])
                    st.write(f"{line} → {domain_status}")