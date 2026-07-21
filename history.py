import json
import os

def load_history():
    if not os.path.exists("history.json"):
        with open("history.json","w") as file:
            json.dump([],file)

    with open("history.json","r") as file:    
        return json.load(file)

def save_history(data):
    with open("history.json","w") as file:
        json.dump(data,file,indent=5)

def clear_history():
    save_history([])
    