from fastapi import FastAPI,HTTPException
from modelImport import load_models
from predict import predictIt
from pydantic import BaseModel

app = FastAPI()

class Text(BaseModel):
    text : str

@app.post("/predict")
def predictFR(text:Text):
    req = load_models()
    output = predictIt(text=text.text,model=req["model"],le=req["le"],vectorizer=req["vectorizer"])
    return output


