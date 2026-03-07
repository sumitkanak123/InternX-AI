from langchain_huggingface  import HuggingFaceEmbeddings    
em=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")   

#Documents many types quetions
user_docs= [
    "Taj Mahal is in Agra, India.",
    "The Colosseum is in Rome, Italy.",
    "The Eiffel Tower is in Paris, France."
]   
#User Query select as my choice
user_query="where is the eiffel Tower"  # if we want to change my documents quetion then similarly change user_query are diffre

user_docs_embeddings=em.embed_documents(user_docs)
query_embedding=em.embed_query(user_query)  
print("Document Embeddings:", user_docs_embeddings)

#compite similarity

from sklearn.metrics.pairwise import cosine_similarity  # use for model measure, sklearn is ML library

similarities=cosine_similarity([query_embedding], user_docs_embeddings) # when we have many numbers like vectors then use of cosine simikilarity

print("Similarities:", similarities) 
print("Most similar document:", user_docs[similarities.argmax()])   

similarities = similarities[0]

print("Similarities:", similarities)

# Best match
best_score = max(similarities)
best_index = similarities.tolist().index(best_score)

throshold=0.5
print('Similarity score:',  best_score)

if best_score < throshold:
    
    print("I don't know")
else:
    print("answer found", user_docs[best_index])


# if similarity <0.5: then print("I don't know") if similarity >0.5: print(most similar document)nt from user_query