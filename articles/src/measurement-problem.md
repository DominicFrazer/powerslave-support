# AI made our measurement problem worse, not better.

**Dominic Frazer-Imregh**
*Published on LinkedIn, 10 August 2026*

---

For six months I've been telling anyone who'd listen that AI has made the typing free. That my CEO ships his own POCs. That my QA fixes her own bugs. That the fifteen-year gap between having an idea and having it running is now closed to something like fifteen minutes.

All of that is still true. But there is a dark layer that I haven't talked about yet.

The observation is this: **AI accelerates whatever direction you're pointed in. Including the wrong one. Including deeper into a hole you didn't realise you were in.** Building a basic feature or fixing a reproducible bug is straightforward. Fixing something that resists diagnosis is a different game entirely.

I've seen it play out more than once over the last year. A team spends weeks with Claude, producing thousands of lines of thoughtful, well-commented code, addressing what looks like a real problem. The commit messages are excellent. The reasoning in each individual change is defensible. The code compiles. Every single one of the fixes makes local sense.

And sometimes the signal the fixes are reacting to is wrong. Not slightly wrong. Categorically wrong — the sensor is measuring one thing and reporting it as another, and every downstream fix is calibrated against a lie the system is telling itself. Claude amplifies the problem by being agreeable — keen to help, keen to find a reason the current theory could be right, keen to propose the next fix in the same direction.

In the old world, this used to catch itself. When each fix took a week to type, there was time between attempts to notice that the last one hadn't worked. Someone would say, out loud, "wait, we're chasing a symptom, not a cause." The cost of the next attempt was high enough to force a re-examination.

With AI, the next attempt costs nothing. So there is no natural pause. Teams ship fix after fix, each locally reasonable, each addressing a symptom of the same underlying broken measurement, and the direction is away from the problem, not towards it. Weeks in, they're not closer to a solution — they're further from one, because they've built structural machinery around the wrong signal, and that machinery has to be unwound before any real progress can happen.

The single sentence that captures it: **the tool that's meant to fix the problem becomes the thing producing the data that makes the problem look real.** You can't tell whether the fix is working, because the sensor telling you whether it's working is the same thing that needed fixing.

That's not an AI-specific pattern. It's an old engineering trap. But AI makes it much worse for one specific reason: it removes the natural circuit breaker of typing time.

Typing was the friction that used to make you stop and think. It's gone now. What replaces it is not obvious, and most teams — including good teams — haven't worked it out yet. The pressure to deliver fast, because it's AI-supported, only makes the problem worse.

**Three signs your team may be in this pattern.**

The fixes are cumulative rather than convergent. Each week adds new mechanisms and none of them replaces an old one. Instead of the code getting simpler as you understand the problem better, it gets more elaborate. Every fix is another layer of control rather than a removal of a false one. If you look at last month's PRs and none of them delete anything, you're not converging. You're adding epicycles.

The team defends individual commits rather than the direction. When someone asks "is this working?" the answer is a story about the last three changes. The changes themselves are described in terms of what they do, not whether they've moved the underlying problem. Nobody says "the metric is X and we've moved it from A to B." Nobody says it because there is no metric, or because the metric is the broken thing, or because nobody has committed to which metric would be the honest one.

The commits are excellent, and the project is not shipping. This is the most disorienting version of the pattern. Every code review is easy to approve. Every commit message is clear. Each merged PR looks like a step forward on its own terms. And nothing gets to production, because none of it is production-ready in the aggregate.

**The lesson underneath.**

The value of a senior engineer used to be in the writing of the code. It has now moved almost entirely into three places, and they're the three places that AI does not do for you.

Deciding what to measure. Naming the metric that will tell you whether your changes are working, and committing to it. This is boring. It looks like planning theatre. It is the single most valuable thing a senior engineer does now, because without it, all subsequent typing is directional acceleration without a direction.

Watching what you built as if you didn't build it. The engineer who is genuinely useful in an AI-heavy workflow is not the one who writes the most, but the one who periodically stops and asks "is what I've built doing what I thought it would?" This is not testing. Testing is a different discipline. This is a stance — a willingness to look at your own recent work with suspicion, to treat it as evidence against your original hypothesis rather than for it.

Being willing to bin weeks of work. When the measurement was wrong, most of what was built is wrong too — not because it's badly written, but because it was built against a false signal. In the old world, weeks of typing produced enough sunk cost that you'd try to salvage it. In the new world, weeks of typing cost almost nothing to reproduce, and salvaging the wrong direction is often more expensive than starting over. Being able to say "this doesn't merge; we start again" is a senior skill that used to be almost impossible to justify and is now often the correct call.

**The uncomfortable version of the observation.**

The engineers most at risk from this pattern are not the junior ones. Junior engineers get their PRs reviewed, get told when they're chasing symptoms, get slowed by their own inexperience. The engineers most at risk are the ones who've earned the right to ship without much oversight. Give a confident senior person AI tools and a genuinely hard problem — one where the underlying measurement is wrong — and you get weeks of increasingly elaborate machinery, none of which is stupid on its own, all of which will need to be undone.

I've written articles about how AI has flattened the hierarchy between senior and non-senior engineers. That's still true. But the failure mode of a non-senior person with AI tools is that they ship something small and wrong that gets caught quickly. The failure mode of a senior person with AI tools is that they ship something impressive and wrong, that takes weeks to catch, because everyone assumed the senior person had checked the measurement.

**A small habit I've adopted.**

Before starting anything non-trivial with Claude, I write down — in one paragraph — what I would need to see in the world for the work to be done. Not a spec. Not acceptance criteria. Just: "if this works, X will move from A to B, and I will see it in this log line." Then I keep that paragraph in mind while working.

Most of the time this is unnecessary — the work is small enough that the metric is obvious. But when it turns out to be necessary, it is the thing that stops the drift. It's boring, it takes ten minutes, and it is the single most valuable habit I have adopted since I started working with Claude.

---

I've spent nine articles telling you that AI has made the typing free. I'm not taking any of it back. But free doesn't mean cheap. Somebody still has to know where the target is.
