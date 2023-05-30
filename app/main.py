import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

class Word(BaseModel):
    word: str

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict_length(word: Word):
    length = len(word.word)
    result = {"length": length}
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)