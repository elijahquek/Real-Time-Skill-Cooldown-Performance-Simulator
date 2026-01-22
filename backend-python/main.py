from fastapi import FastAPI
from models import SkillRequest
from logic import evaluate_skill, load_config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate")
def evaluate(req: SkillRequest):
    result = evaluate_skill(req.stamina)
    return { "result": result }

@app.post("/log")
def log_event(event: dict):
    print("EVENT:", event)
    return { "ok": True }

@app.get("/config")
def get_config():
    return load_config()