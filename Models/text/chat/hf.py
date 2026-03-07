from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from dotenv import load_dotenv 
load_dotenv()

endpoint=HuggingFaceEndpoint(repo_id="google/gemma-3-270m-it", task="text-generation")
chatmodel=ChatHuggingFace(llm=endpoint)
result=chatmodel.invoke("where is the eiffel Tower")
print(result)


print(result.content)