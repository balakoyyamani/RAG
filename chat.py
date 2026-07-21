from rag_service import get_embed , get_query, get_AI_response, create_collection,add_collection
from history import load_history,save_history,clear_history


system_prompt="""you are the good assist bot for me 
                give solution in single statement
                don't generate the sysmbols like *,# with the response"""
about_me = [
    "Balachandar Koyyamani",
    "B.Tech Information Technology",
    "Panimalar Engineering College",
    "Anna University",
    "CGPA 8.68",
    "Chennai, Tamil Nadu",
    "Software Engineer Aspirant",
    "Preparing for Campus Placements",
    "Java"
    ]
collection=create_collection("collection")
doc_vector=get_embed(about_me)
add_collection(collection,doc_vector,about_me)
while True:
    history=load_history()
    usr_msg=input("user : ").strip()
    if not usr_msg:
        print("Enter the message")
        continue
    if usr_msg=="/exit":
        print("Thank you for chat")
        exit()
    history.append(f"user : {usr_msg}")
    
    query_vector=get_embed(usr_msg)
    embedd_response=get_query(collection,query_vector,3)
    context="\n\n".join(embedd_response["documents"][0])
    history_text="\n\n".join(load_history())
    prompt=f"""{system_prompt}
                history:
                {history_text}
                context:
                {context}
                question:
                {usr_msg}"""
    Ai_assist=get_AI_response(prompt)
    print(f"AI assist : {Ai_assist}")
    history.append(f"AI assist : {Ai_assist}")
    save_history(history)
    
    


    


