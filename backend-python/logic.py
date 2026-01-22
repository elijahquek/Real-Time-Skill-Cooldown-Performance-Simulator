import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def evaluate_skill(stamina: float):
    config = load_config()
    return {
        "rating": "Perfect" if stamina > 70 else "Normal",
        "cooldown": config["cooldown_time"],
        "stamina_cost": config["stamina_cost"]
    }