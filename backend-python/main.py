from fastapi import FastAPI
from models import SkillRequest
from logic import evaluate_skill

app = FastAPI()

@app.post("/evaluate")
def evaluate(req: SkillRequest):
    result = evaluate_skill(req.stamina)
    return { "result": result }