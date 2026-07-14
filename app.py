from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# 加载模型（启动时加载一次）
model = joblib.load("model.pkl")

class Request(BaseModel):
    text: str

@app.get("/")
def hello():
    return {"message": "Hello from MLOps!"}

@app.post("/predict")
def predict(req: Request):
    # 预测
    proba = model.predict_proba([req.text])[0]
    pred = int(model.predict([req.text])[0])
    
    return {
        "input": req.text,
        "prediction": "positive" if pred == 1 else "negative",
        "confidence": float(proba[pred]),
        "probabilities": {
            "negative": float(proba[0]),
            "positive": float(proba[1])
        }
    }