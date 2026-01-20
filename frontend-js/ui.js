import { state } from "./state.js";

export function render() {
  document.getElementById("cooldown").innerText =
    state.skillReady ? "Skill Ready" : `Cooldown: ${state.cooldown.toFixed(1)}`;

  document.getElementById("result").innerText =
    `Stamina: ${state.stamina.toFixed(1)}`;
}
