// Page 02 — Regex Rules.  Owner: M10
import * as api from "./api.js";

export function init() {
  window.addEventListener("langchange", () => render(false));
}
export async function show() {
  // TODO(M10): fetch api.rules() once, then render(true)
  void api;
}
function render(animate) {
  // TODO(M10):
  //  [ ] A · legend of syntax colours (look, named, backref, cls, quant, escape, alt)
  //  [ ] B · one glass card per rule: number badge in rule colour, label (th/en), tags
  //      (weight, target, flags), highlighted pattern from `tokens`, explain list, example -> masked
  //  [ ] last card spans the full row when the count is odd; cards rise in with a stagger
  void animate;
}
