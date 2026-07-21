from config import client,text_model,embed_model,client_db

def get_embed(data):
    response=client.models.embed_content(
        model=embed_model,
        contents=data
    )
    print("Embedded successful")
    
    return [embed.values for embed in response.embeddings]

def create_collection(name):
    collections=client_db.create_collection(name=name)
    print("collection created")
    return collections

def add_collection(collections,embeddings,documents):
    ids=[f"{i}" for i in range(1,len(documents)+1)]
    collections.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
        )
    print("collection added")

def get_query(collections,query_vector):
    response=collections.query(
        query_embeddings=query_vector,
        n_results=2
    )
    print("query recieved")
    print(response["documents"][0])
    return response
           

def get_AI_response(prompt):
    response=client.models.generate_content(
        model=text_model,
        contents=prompt
    )
    print("AI response recieved")
    return response.text
    