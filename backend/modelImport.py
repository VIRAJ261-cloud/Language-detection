import pickle
import os
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
PATH = os.getcwd()
PATH = os.path.dirname(PATH)

def load_models():
    with open(os.path.join(PATH,"models","model.pkl"),"rb") as f:
        model = pickle.load(f)

    with open(os.path.join(PATH,"models","le.pkl"),"rb") as f:
        le = pickle.load(f)

    with open(os.path.join(PATH,"models","vectorizer.pkl"),"rb") as f:
        vectorizer = pickle.load(f)

    return {"model":model,
            "le":le,
            "vectorizer":vectorizer}