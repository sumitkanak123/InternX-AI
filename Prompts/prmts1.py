from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

endpoint= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    
    )
cm=ChatHuggingFace(llm=endpoint)    

Topic=input("Enter your topic: " )
number_of_lines=input("Enter number of lines: " )
style=input("Enter your style: " )
language=input("Enter your language: " )    
print()
system_prompt = f"In {Topic}, explain the major components and describe the working principle of each component in strictly {number_of_lines} lines. Use {style} terminology and write in {language}."

result=cm. invoke(system_prompt)
print(result.content)

