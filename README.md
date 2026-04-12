# 🌐 Language Detection Project

A Machine Learning-based **Language Detection System** that identifies the language of a given text input.

---

## 🚀 Features
- Detects language from input text  
- Uses Machine Learning algorithms  
- Simple and easy to use  
- Trained on a real-world dataset  

---

## 📂 Project Structure

```
Language-detection/
│
├── backend/
│   ├── cleanTxt.py
│   ├── main.py
│   ├── modelImport.py
│   └── predict.py
│
├── data/
│   └── Language Detection.csv
│
├── models/
│   ├── le.pkl
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   └── detect.ipynb
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/VIRAJ261-cloud/Language-detection.git
cd Language-detection
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create Data Folder (if not present)

```bash
mkdir data
```

---

### 4. Download Dataset

Download the dataset from Kaggle:  
https://www.kaggle.com/datasets/basilb2s/language-detection

After downloading:
- Extract the dataset  
- Rename the file to: `Language Detection.csv`  
- Place it inside the `data` folder  

---

### 5. Run the Backend Server

```bash
cd backend
uvicorn main:app --reload
```

---

### 6. Test the API

Use Postman to test the `/predict` endpoint:

- Method: **POST**  
- Body (JSON):

```json
{
    "text": "Your_text_here"
}
```

---

## ⚠️ Important Notes
- File name must be exactly: `Language Detection.csv`  
- File must be inside the `data` folder  
- The project will not run without the dataset  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- FastAPI  
- Machine Learning  

---

## 📌 Future Improvements
- Add web interface (Flask / Streamlit)  
- Improve model accuracy  
- Add support for more languages  