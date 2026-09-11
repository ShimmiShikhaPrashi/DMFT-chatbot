from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from chatbot import get_response

app = FastAPI(title="DMFT Chatbot API")


class ChatMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/chat")
def chat(data: ChatMessage):
    response = get_response(data.message)

    return {
        "user_message": data.message,
        "bot_response": response
    }


app.mount("/static", StaticFiles(directory="static"), name="static")