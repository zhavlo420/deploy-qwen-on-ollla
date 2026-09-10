from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama


app=FastAPI() #http acess

#cors o allow fronend access

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   
    allow_methods=["*"],
    allow_headers=["*"],)
class ChatRequest(BaseModel):
    message:str
    model:str
@app.post("/chat")
async def chat(request:ChatRequest):
    try:
        response=ollama.chat(model="qwen2.5",messages=[{"role": "user", "content": request.message}])
        return {"response":response["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
    
@app.get("/")
def home():
    return {"message":"Welcome to the Ollama Chat API"} 

#curl +X POST "http://0.0.0.0:8000/chat" "Content-Type: application/json" -d '{"message": "hello"}'