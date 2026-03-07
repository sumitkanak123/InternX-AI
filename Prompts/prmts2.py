from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

endpoint= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
)
st.header("AI Technical assistant")     
    
cm=ChatHuggingFace(llm=endpoint)    

Topic=st.text_input("Enter your topic: " )
number_of_lines=st.number_input("Enter number of lines: " )
style=st.text_input("Enter your style: " )
language=st.text_input("Enter your language: " )    
print()
system_prompt = f"In {Topic}, explain the major components and describe the working principle of each component in strictly {number_of_lines} lines. Use {style} terminology and write in {language}."

if st.button("Generate"):
    result=cm. invoke(system_prompt)
    st.write(result.content)    

