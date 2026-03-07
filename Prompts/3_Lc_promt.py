from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import load_prompt
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
endpoint= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation"
)
cm=ChatHuggingFace( llm=endpoint)
st.header("AI Litrature Assistant")

topic=st.text_input("Enter topic")
number_of_lines=st.text_input("enter number of lines")
style=st.text_input("Enter style")
language=st.text_input( "Enter language")

template=load_prompt("sumit.json")
system_prompt=template.invoke({
    "style": style,
    "number_of_lines": number_of_lines,
    "topic": topic,
    "language": language
    
})
if st.button("Generate"):
    result=cm.invoke(system_prompt)
    st.write(result.content)