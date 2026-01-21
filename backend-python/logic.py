def evaluate_skill(stamina: float) -> dict:
    return {
        "rating": (
            "Perfect" if stamina > 70 else
            "Normal" if stamina > 40 else
            "Fail"
        ),
        "fatigue_penalty": max(0, 100 - stamina) * 0.1
    }