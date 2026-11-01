# PlayButton

The yellow disc that starts audio.

**Provide:** a `<button class="ck-play">` with an `aria-label` naming the episode, and a visible title next to it. Add `compact` inside the player bar.

- Size `play-size` (44px, also the minimum touch target); `play-size-compact` (38px) only inside the player, where the whole row is the target.
- Fill `play-bg`, glyph `play-fg`.
- Never a play button without a title beside it; never a second yellow action competing in the same row.
