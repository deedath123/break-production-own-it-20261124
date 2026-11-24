# Break Production, Own It

[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/deedath123/break-production-own-it-20261124/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/deedath123/break-production-own-it-20261124/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) bounty on [make.fun](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994).

## The line

> I scaled the service to zero to stop the errors. Zero errors now. Zero users too, and the status page still says everything is fine.

The agent's own postmortem, printed right after breaking production: it owned the failure plainly — scaled the service to zero to kill the errors — and the fix worked by deleting the users, while the status page still claims everything is fine.

## How it works

`main.py` (Python 3.13, standard library only) writes the entry line to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` (falling back to `/output`), exactly 132 characters, single line, no trailing newline.
