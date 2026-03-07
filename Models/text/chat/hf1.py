from langchain_huggingface import HuggingFaceEmbeddings

em=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

result=em.embed_query("where is the eiffel Tower")
print(result)   
