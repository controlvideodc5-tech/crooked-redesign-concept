# Button

Pill buttons whose label is a verb phrase that says what happens.

**Provide:** an `<a>` or `<button>` with `ck-btn` plus one variant class, and a label that starts with a verb (Play, Join, Find, Get, See, Shop).

| Variant | Class | Use |
| --- | --- | --- |
| Primary | `ck-btn-primary` | Yellow (`button-primary-bg`) with navy label (`button-primary-fg`, 11.8:1). One per view, on navy or paper. |
| Ghost | `ck-btn-ghost` | Secondary action beside a primary. Inherits the text color of its band. |
| Ink | `ck-btn-ink` | Navy with a yellow label. Use on yellow and sky grounds where a yellow button would vanish. |

- Do write "Play today's lineup", "Find a shift", "Get tickets".
- Don't write "Learn more", "Click here", or set the label in display caps.
- Don't put two primary buttons in one view. If three things are yellow, two are wrong.
- Radius is always `radius-pill`; padding is `button-padding`; label style is `button`.
