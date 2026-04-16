from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from modelImport import load_models
from predict import predictIt
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],   
)

class Text(BaseModel):
    text : str

@app.post("/predict")
def predictFR(text:Text):
    req = load_models()
    output = predictIt(text=text.text,model=req["model"],le=req["le"],vectorizer=req["vectorizer"])
    return output


