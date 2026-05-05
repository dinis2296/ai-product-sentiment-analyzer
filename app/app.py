
from fastapi import FastAPI
from predict import predict

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/predict")
def predict_endpoint(title: str):
    prob = predict(title)

    return {
        "title": title,
        "probability": prob,
        "prediction": int(prob > 0.5)
    }
