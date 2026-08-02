# Review scorecard

One row per completed page review. **This file is the point of the whole system.**

The five-reviewer panel and OpenEvidence are different retrieval stacks with
different blind spots. Tracking what OE catches that the panel misses turns the
manual paste step from a gap check into a spot check: after enough rows, the
recurring misses go back into `.claude/agents/*.md` and the panel stops making them.

Read the **"OE caught, panel missed"** column as the backlog for improving the panel.

| Date | Page | Panel HIGH | Panel total | OE caught, panel missed | Panel caught, OE missed | Lesson → which agent |
|---|---|---|---|---|---|---|
| _(first row lands when the first `/page` run ships)_ | | | | | | |

## Standing lessons

Patterns confirmed across more than one review. Each one should already be written
into the named agent definition.

| Lesson | Agent | Status |
|---|---|---|
| Verify approval status, never assume — tolebrutinib got an FDA CRL in Dec 2025 after being written as approved | `recency-scout` | in agent |
| Pull the FDA label rather than recalling a dose | `dose-pharmacist` | in agent |
| EPTS/LOD is the military-box field most often missing site-wide | `military-tricare` | in agent |
| Distinguish FDA vs EMA vs "phase 3 positive, not approved" explicitly | `recency-scout` | in agent |
