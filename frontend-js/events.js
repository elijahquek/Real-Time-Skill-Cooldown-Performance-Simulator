export function emitSkillUsed(data) {
  document.dispatchEvent(new CustomEvent("skillUsed", { detail: data }));
}
