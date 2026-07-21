from google import genai
import chromadb
import os

client=genai.Client(api_key=os.getenv("GOOGLE_API_KEY_ASSIST_BOT_01"))
client_db=chromadb.Client()
text_model="gemma-4-31b-it"
embed_model="gemini-embedding-001"