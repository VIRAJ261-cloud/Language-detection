from cleanTxt import cleanText

def predictIt(text,model,le,vectorizer):
    text = cleanText(text=text)
    vector = vectorizer.transform([text])
    output = model.predict(vector)
    final = le.inverse_transform(output)
    return {
        "Language": final[0],
    }