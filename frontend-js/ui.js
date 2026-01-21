import { state } from "./state.js";

export function render() {
  document.getElementById("cooldown").innerText =
    state.skillReady ? "Skill Ready" : `Cooldown: ${state.cooldown.toFixed(1)}`;

  document.getElementById("result").innerText =
    `Stamina: ${state.stamina.toFixed(1)}`;
}

fetch("http://localhost:8000/log", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    type: "SKILL_USED",
    stamina: state.stamina,
    timestamp: Date.now()
  })
});
