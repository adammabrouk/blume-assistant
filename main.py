import os

import vertexai
from fastapi import FastAPI, HTTPException
from google.oauth2 import service_account
from pydantic import BaseModel
from vertexai.preview.generative_models import GenerativeModel

app = FastAPI()

PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
MODEL_ID = "gemini-2.0-flash-001"


class UserInput(BaseModel):
    user_input: str


@app.on_event("startup")
def startup_event():
    if not all([PROJECT_ID, REGION, SERVICE_ACCOUNT_FILE]):
        raise RuntimeError(
            "PROJECT_ID, REGION, and SERVICE_ACCOUNT_FILE must be set in environment variables."
        )

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE
    )
    vertexai.init(project=PROJECT_ID, location=REGION, credentials=credentials)


@app.post("/vapi-llm")
async def vapi_llm(user_input: UserInput):
    try:
        model = GenerativeModel(MODEL_ID)
        response = model.generate_content(user_input.user_input)
        return {"content": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model error: {str(e)}")


@app.post("/book-appointment")
async def book_appointment():
    return {"message": "Appointment booked successfully"}
