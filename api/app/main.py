from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.candidates import router as router_candidates
from app.routers.resumes import router as router_resumes

from dotenv import load_dotenv
import os
load_dotenv()

CORS_URL = os.getenv("CORS_URL")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(router_candidates)
app.include_router(router_resumes)


@app.get("/")
def home():
    return "Welcome to ResumeFlow AI API"