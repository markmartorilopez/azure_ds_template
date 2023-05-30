import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import Person


app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/metrics")
def get_metrics(person: Person):

    # Query the Azure Lakehouse and retrieve Person's metrics
    # Perform necessary data processing and calculations

    height = 180
    weight = 70
    ranking = 9
    metrics = {"name":person.name,
               "height":height,
               "weight":weight,
               "Outlier Ranking":ranking}
    return metrics


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)