# My CEO built his own battle station.

**Dominic Frazer-Imregh**
*Published on LinkedIn, 2 May 2026*

---

Yesterday my CEO sent me a two-page Claude-generated technical specification. Detailed APIs. Numbered steps. Architecture diagrams in prose form. The whole package, polished and confident, addressed to me and politely titled "Yo, I have spec for you".

He hadn't read it. He didn't need to. This was his Claude project manager speaking.

I skimmed it for about ninety seconds and replied:

*"Nice. Claude is hallucinating, but nice."*

We both laughed.

Now. The old version of me would not have laughed so easily. The old version of me would have done the full Luke Skywalker. Standing on the gantry above Cloud City, hand freshly amputated, ego bruised, learning that the Empire's most fearsome warrior is in fact his dad. *NOOOOOOOOOO.* Throw yourself off into the abyss. Three days of recovery on Dagobah. A whole second film of brooding before you can function again.

What if Luke had joined with his dad? What if that was enough to defeat the evil emperor and then maybe his dad would have turned good in a different way? After all, it turned out alright in the end.

The equivalent in our world: a senior engineer receiving a hallucinated spec from a non-technical CEO and screaming about it and how we can't replace engineers with AI. Long Slack message about why this isn't how you write specifications. Polite but icy meeting to explain that hallucinated APIs are dangerous. A week of low-grade resentment. And a LinkedIn post titled *"Why your CEO shouldn't be writing specs with AI."*

But what if Luke had paused on that gantry, considered for a moment, and said: *"Oh. Cool. That's interesting. Let me think about that"*?

Much shorter film. Probably worse film. But infinitely more productive week.

That's what we did.

I knew what my CEO was actually working on, because we'd already discussed it, and if I didn't know then I would have asked more questions. I summarised the real scenarios in two lines. Then I went to my own Claude — which has visibility of our entire back-end — pointed it at the services we already have, the scenarios we'd already produced, and asked it to *just check a few things*.

It confirmed that no code was needed at all. We had everything. What was needed was a clean document explaining how to do, with what already existed, the thing the CEO wanted to do.

The document needed one tweak. My Claude had decided, on a technical level, that the user-agent header could be safely dropped — non-breaking, harmless. My CEO needed it. So we tweaked. Updated. Handed back. All Claudes happy. Total time elapsed between the spec arriving and the corrected document being ready: about twenty-five minutes.

For those of you still standing on the gantry, let me say this clearly: **this entire interaction was impossible five years ago.**

Five years ago, my CEO would never have produced a spec at all. He'd have come to me with a vague description and a deadline. I'd have gathered requirements over two weeks of meetings. Estimated three months. A team of four would have built something close to but not exactly what he meant. He'd have seen it, said *"not quite"*, and we'd have iterated for another month. The fully operational battle station, after all, is not built in a day — not in the 1983 film, not in an office in 2021.

In 2026 it is.

*That's* the trade-off worth seeing clearly. He burnt some Claude tokens drafting a spec. I burnt fifteen minutes of attention reading it and another ten producing the answer. The total cost is rounding-error compared to a six-week project. The fact that his spec was largely hallucinated, that I discarded most of it, that he hadn't even read it — none of that matters. The cheap stuff is allowed to be wasted now. That's what cheap means.

---

Let me tell you a different story, from a different time.

Mid-1990s. I'm on a trade stand at an industry show, demonstrating an EPoS system for cafeterias and small retailers. A professor approaches the stand. Tweed. Confidence. He's been deputised by his university to choose a point-of-sale system for the staff cafeteria, and he has arrived — in the most literal sense possible — with a full PC computer specification in his head.

He scoffs at our hardware. The CPU is too slow. The storage is too small. He had imagined something much more impressive. Something more befitting a university procurement.

My question is simple. *"How many products do you sell in the cafeteria?"*

His answer: *"200 megabytes."*

I try again. *"No — how many products. Not how much storage."*

His answer, again: *"200 megabytes."*

In Star Wars terms, this was the moment Obi-Wan waves his hand and says *"these aren't the droids you're looking for."* In the film, the stormtrooper's mind is weak and the Force does its work. The stormtrooper had probably seen hundreds of droids that day and wasn't really bothered. In real life, the professor's mind was clouded by his own pre-conceived assumptions. The Force does not work on people who already know the answer. They have no model of what they don't know, so there's no gap for the suggestion to enter.

We lost the sale. I didn't care. The professor was as bad at shooting as a stormtrooper. Laser blaster nicely dodged.

---

While rewatching old Star Wars films, here's what I've been chewing on since the spec landed in my inbox.

The professor and the CEO are doing the same thing, thirty years apart. Both of them are non-technical people trying to specify a technical system. Both of them turned up with the wrong unit of measurement — the professor counted in megabytes, the CEO counted in API endpoints — because neither of them was being asked to think in the right unit, which was scenarios.

The difference is that in 1995, when the translation broke, there was nowhere for it to go. The professor couldn't answer my question. I couldn't guess his cafeteria's product count. The conversation ended. He went back to his university and presumably bought something twice the size and 5 times the cost that he needed.

In 2026, when the translation breaks, there's a Claude on each side patching it up. His Claude generates the spec he doesn't need. My Claude reads the back-end he doesn't know we have. I sit between them, reading both, spotting where they're wrong, fixing the bits that matter, and shipping the answer.

**The technical person's job hasn't disappeared. It's moved.** Thirty years ago, my job was to translate the professor's vague needs into a working spec, and I couldn't, because he had no model of what he didn't know. Today, part of my job is to read what two AIs have drafted, decide which bits are right, and hand back the corrected version. Different job. Faster, lower-stakes, impossible to imagine before now.

Most senior engineers I know are still standing on the gantry, screaming *NOOOOOOOOOO* at the AI-generated specs landing on their desks. They want to fall off. They want to lecture about hallucinations and architectural integrity and the right way to gather requirements. They want their non-technical colleagues to *learn how to write a proper spec.*

I used to want that too. Now I think: just chuckle, fix the document, hand it back, get on with the day. The laser blast you're trying to dodge isn't coming for you. It's a pretend laser, fired by a Claude that hasn't read the codebase, at a CTO who has. The damage it can do is fifteen minutes of your time. The cost of treating it as a real blast is your weekend, your relationship with your CEO, and a reputation as the engineer who won't move with the times.

My CEO built his own battle station. I helped him aim it. He shipped a feature. No one wrote a line of code. All in less time than it would have taken to schedule a meeting about it five years ago. Nobody screamed. Nobody fell off any gantries.

The Empire would be confused. So would my old colleagues.

I'm fine with both.
