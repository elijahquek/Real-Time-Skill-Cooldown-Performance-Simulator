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
    try:
        result = evaluate_skill(req.current_stamina, load_config())
        return result
    except ValueError as e:
        return {
            "success": False,
            "error": str(e)
        }

@app.post("/log")
def log_event(event: dict):
    print("EVENT:", event)
    return { "ok": True }

@app.get("/config")
def get_config():
    return load_config()