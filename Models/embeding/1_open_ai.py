from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding_model= OpenAIEmbeddings(model= "text-embedding-3-small",dimensions=32)

vectors_result= embedding_model.embed_query("What is the capital of France?")   
print(vectors_result)
