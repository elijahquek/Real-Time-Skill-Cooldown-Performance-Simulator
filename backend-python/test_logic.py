import pytest
from logic import evaluate_skill

VALID_CONFIG = {
    "cooldown_time": 20,
    "stamina_cost": 50
}

def test_skill_success():
    result = evaluate_skill(100, VALID_CONFIG)

    assert result["success"] is True
    assert result["cooldown_time"] == 20
    assert result["stamina_remaining"] == 50

def test_insufficient_mana():
    result = evaluate_skill(10, VALID_CONFIG)

    assert result["success"] is False
    assert result["reason"] == "INSUFFICIENT_STAMINA"

def test_negative_stamina_cost_rejected():
    bad_config = {
        "stamina_cost": -5,
        "cooldown_time": 50
    }

    with pytest.raises(ValueError):
        evaluate_skill(100, bad_config)

def test_zero_cooldown_time_rejected():
    bad_config = {
        "stamina_cost": 10,
        "cooldown_time": 0
    }

    with pytest.raises(ValueError):
        evaluate_skill(100, bad_config)