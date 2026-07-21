from config import client,text_model,embed_model,client_db

def get_embed(data):
    response=client.models.embed_content(
        model=embed_model,
        contents=data
    )
    
    return [embed.values for embed in response.embeddings]

def create_collection(name):
    collections=client_db.create_collection(name=name)
    return collections

def add_collection(collections,embeddings,ids,documents):
    collections.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
        )

def get_query(collections,query_vector):
    response=collections.query(
        query_embeddings=query_vector,
        n_results=2
    )
    return response
           

def get_AI_response(prompt):
    response=client.models.generate_content(
        model=text_model,
        contents=prompt
    )
    return response.text
    