# QA checklist

*Owner: M05.* Run on Chrome, Safari/Firefox, and a phone-width window, in TH and EN, light and dark.

TODO(M05): expand. Starting points:

- [ ] Assignment sample masks exactly as the spec
- [ ] Upload utf-8 and Windows-874 Thai files; drag & drop works; oversize file shows an error
- [ ] Every rule toggle on/off updates both panes and stats
- [ ] Copy and download produce the masked text
- [ ] Source log grows with content and stops at 72vh
- [ ] Test Suite shows all cases passing; try-it box masks live
- [ ] DFA: every sample chip gives the expected ACCEPT/REJECT
- [ ] Language and theme are remembered after reload
- [ ] No layout overflow at 390px width
