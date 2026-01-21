import { state } from "./state.js";
import { emitSkillUsed } from "./events.js";
import { render } from "./ui.js";

let CONFIG = null;

async function loadConfig() {
  const res = await fetch("http://localhost:8000/config");
  CONFIG = await res.json();
}

await loadConfig();

document.getElementById("skillBtn").onclick = async () => {
  if (!state.skillReady) return;

  if (state.skillState === SkillState.READY) {
  state.skillState = SkillState.COOLDOWN;
  state.cooldown = CONFIG.cooldown_time;
  }
  
  state.stamina -= CONFIG.stamina_cost;

  emitSkillUsed({
    stamina: state.stamina
  });

  // Ask backend to evaluate success
  const res = await fetch("http://localhost:8000/evaluate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ stamina: state.stamina })
  });

  const data = await res.json();
  document.getElementById("result").innerText = data.result;
};

function update(delta) {
  if (state.skillState === SkillState.COOLDOWN) {
  state.cooldown -= delta;
  if (state.cooldown <= 0) {
    state.skillState = SkillState.READY;
  }
}
  render();
}

let last = performance.now();
function loop(now) {
  update((now - last) / 1000);
  last = now;
  requestAnimationFrame(loop);
}

loop(last);
