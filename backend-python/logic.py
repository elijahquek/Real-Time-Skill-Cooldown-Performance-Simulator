import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def validate_config(config: dict):
    if config["cooldown_time"] <= 0:
        raise ValueError("cooldown_time must be >= 0")
    if config["stamina_cost"] <= 0:
        raise ValueError("stamina_cost must be > 0")
    
def evaluate_skill(stamina: float, config: dict) -> dict:
    validate_config(config)

    if stamina < config["stamina_cost"]:
        return {
            "success": False,
            "reason": "INSUFFICIENT_STAMINA"
        }

    return {
        "success": True,
        "cooldown_time": config["cooldown_time"],
        "stamina_remaining": stamina - config["stamina_cost"]
    }