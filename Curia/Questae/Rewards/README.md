# 🏆 Rewards — crystallized experience

> *A questa is the quest. A Reward is what the party carries out of it. The
> quest file is a record of a problem; the Reward is the lesson, written so it
> is useful to someone who never saw the problem.*

A Reward is minted at the end of rule 7 in `../README.md`: a questa sits in
`Solved/` until a distillation dialog with Julio confirms the lesson, a
`REW-####` file is written here, and **the questa file is deleted**.

## What a Reward is for

The questa answers *what went wrong and where*. The Reward answers *what we
now know*. It outlives the code it came from, so it is written for a reader
with no context: no file/line archaeology, no session history, no assumption
that the bug still exists.

Because minting a Reward **deletes** its questa, the Reward has to carry
everything from that quest still worth having — including reasoning that was
not the quest's stated purpose. A lesson dropped here is a lesson lost.

## Shape

```
# REW-#### — <the lesson, stated as a claim>

- **From:** QST-#### (title)
- **Distilled:** YYYY-MM-DD, with Julio
- **Applies to:** <where this bites again>

## The lesson
## Why it is not obvious
## What to do differently
## Council / provenance
```

State the lesson as a **claim**, not a topic: "uncommitted prose is already
lost", not "notes on committing prose". A title that makes an assertion can be
agreed with, argued against, and remembered.

## Numbering

`REW-####-short-slug.md`, its own incrementing sequence, independent of the
questa numbers — one questa can be worth no Reward, and a Reward can distil
more than one closed quest. The source quest is named in the `From:` header
rather than in the id.

> **Open for Julio:** the alternative is mirroring the questa number
> (`QST-0080` → `REW-0080`), which is more traceable but breaks as soon as two
> quests distil into one lesson. REW-0001 starts the independent sequence; say
> the word and it renumbers.
