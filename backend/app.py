from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import datetime
import random

app = FastAPI()

def detect_anomaly(transaction):
    #Replace this with your AI model logic
    if transaction["amount"] > 500:
        return random.randint(70, 95)
    else:
        return None

@app.post("/detect_fraud")
async def detect_fraud(request: Request):
    data = await request.json()
    transaction = data['transaction']
    anomaly_score = detect_anomaly(transaction)

    if anomaly_score:
        return JSONResponse({'anomaly_score': anomaly_score, "bot_response": f"This transaction has been flagged. Risk score: {anomaly_score}%. Is it legitimate?"})
    else:
        return JSONResponse({'anomaly_score': None, "bot_response": "Is this transaction legitimate?"})
