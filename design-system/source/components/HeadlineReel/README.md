# HeadlineReel

An animated rotator that cycles the campaign headlines, two beats at a time: the first beat in paper, the turn in yellow.

**Provide:** a list of headlines as `[eyebrow, first beat, second beat]`. Keep each beat to six words or fewer, and keep the brand line ("Less doom. More doing.") first.

- Pace is slow on purpose so each line lands: the current headline fades out over 650ms, the next one's first beat fades up over 1s on `cubic-bezier(.16, .8, .24, 1)`, the yellow turn follows 700ms later, and the headline holds for 6.5s. A yellow progress bar shows the hold.
- Always ship the pause button and the dots. The reel also pauses on hover and while anything inside has keyboard focus. Picking a dot pauses it on that headline.
- Under `prefers-reduced-motion` nothing moves: the reel renders as a static list of every headline.
- Navy ground (`c-navy-900`) with the halo pattern; eyebrow in `c-slate-300` mono caps; second beat `c-yellow-500`. Never more than one reel per page, and it doesn't play under the Crooked Con band.
- The live screen reader region announces the current headline; the pause button's label switches between "Pause headlines" and "Play headlines".
- Current set: Less doom. More doing. · Huge portions. Tiny priorities. · The price is wrong. · Check, please. · Don't let the midterms be mid. · Billionaires don't clip coupons. · Drain the swamp? They put in a hot tub. · Groceries cost a fortune. Voting's still free. · Midterms Tuesday. Make it a short term. Retire the midterm lines after Nov 3.
