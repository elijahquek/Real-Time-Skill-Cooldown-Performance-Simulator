def evaluate_skill(stamina: float) -> str:
    if stamina > 70:
        return "Perfect Execution"
    elif stamina > 40:
        return "Normal Execution"
    else:
        return "Failed Execution"
