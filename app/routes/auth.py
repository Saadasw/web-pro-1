from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#from config.firebase_config import auth
#

import pyrebase
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "databaseURL": ""  # Firebase Realtime DB (optional)
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

#

app = FastAPI()

class User(BaseModel):
    email: str
    password: str

@app.post("/signup")
async def signup(user: User):
    try:
        # Create a new user in Firebase Authentication
        new_user = auth.create_user_with_email_and_password(user.email, user.password)
        return {"uid": new_user['localId']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
async def login(user: User):
    try:
        # Verify the user's credentials
        user_record = auth.sign_in_with_email_and_password(user.email, user.password)
        return {"uid": user_record['localId']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#if __name__ == "__main__":
if True:
    import uvicorn
    

    uvicorn.run(app, host="127.0.0.1", port=8000)
