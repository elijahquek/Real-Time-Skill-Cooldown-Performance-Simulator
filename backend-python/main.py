from fastapi import FastAPI
from models import SkillRequest
from logic import evaluate_skill
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