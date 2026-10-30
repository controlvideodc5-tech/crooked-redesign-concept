# LivePill

Red pill that marks audio or an event that is live right now.

**Provide:** `<span class="ck-live">` with a one- or two-word label; add `pulse` only while audio is actually live or playing.

- Fill `status-live`, white text at 12px bold minimum (4.2:1 qualifies as large-ish UI text only at that weight). The concept's 9px pill failed; don't go smaller.
- For red *text* (an eyebrow, an alert) use `status-live-text`, never `status-live`.
- Pulse stops under `prefers-reduced-motion`.
