// Page 04 — Regex -> DFA visualiser.  Owner: M10
// IMPORTANT: no JavaScript regex here — simulate the DFA by comparing characters directly.
//
// The DFA to draw (minimal DFA for the card / phone patterns, see docs/ARCHITECTURE.md#dfa):
//   prefix group  ->  split into 3 branches by the first separator ("-", " ", none)
//   -> the branches MERGE before the last group (those states are equivalent)  ->  accept.
// Equivalent regex (card): \d{4}(?:-\d{4}-\d{4}-|\x20\d{4}\x20\d{4}\x20|\d{8})\d{4}
// Equivalent regex (phone): 0[1-9]\d(?:-\d{3}-|\x20\d{3}\x20|\d{3})\d{4}

/** groups e.g. card = [[d,d,d,d],[d,d,d,d],[d,d,d,d],[d,d,d,d]] ; symbols: "d" digit, "nz" 1-9, or a literal char */
export function buildDFA(groups) {
  // TODO(M10): return {states:[{id,row,col}], transitions:[{from,to,sym}], accept}
  throw new Error("M10: buildDFA");
}

/** Return the list of visited states for `input` (-1 = dead). */
export function simulate(dfa, input) {
  // TODO(M10)
  throw new Error("M10: simulate");
}

export function init() {}
export function show() {
  // TODO(M10):
  //  [ ] machine selector (card / phone), input + sample chips, tape with moving head
  //  [ ] SVG: states, labelled edges, lane labels, dead state, accepting double circle (scale to width)
  //  [ ] play / step / reset / speed; delta(q, a) = q' readout; ACCEPT pulse / REJECT shake
  //  [ ] equivalent regex + "reading the diagram" cards (th/en)
}
