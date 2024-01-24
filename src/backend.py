from fastapi import FastAPI, HTTPException
from use_model import get_llm
from create_chain import create_chain
from check_model import is_directory_empty, download_llm
import os
import torch
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class RequestData(BaseModel):
    user_input_prompt: str
    question: str


def load_model(template):
    if is_directory_empty():
        print("Creating a directory and downloading the model locally.")
        download_llm()
    torch.cuda.empty_cache()
    model = get_llm()
    retriever = create_chain(model, template)
    print(f"Model {os.listdir('./model/')} has been loaded.")
    return retriever


@app.get("/")
def read_root():
    return {"message": "Hello, this is the FastAPI backend."}


@app.post("/generate_answer")
async def generate_answer_endpoint(request_data: RequestData):
    prompt = request_data.user_input_prompt
    question = request_data.question
    try:
        retriever = load_model(prompt)
        result = retriever.invoke(question)["result"]
        torch.cuda.empty_cache()
        return {"answer": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
