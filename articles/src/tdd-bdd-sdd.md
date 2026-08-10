# TDD. BDD. And the one that's actually doing the work now: SDD.

**Dominic Frazer-Imregh**
*Published on LinkedIn, 25 April 2026*

---

For twenty years we've peacocked about the best ways to develop software. Test-Driven Development said write the test first, watch it fail, make it pass, refactor. Behaviour-Driven Development said wrap the test in a sentence a product manager could read — Given / When / Then — and call it a specification.

Both were trying to do the same thing: pin down what the software is supposed to do before you build it. Both got buried in the syntax of doing it — a developer's heaven!

TDD turned into a ceremony. Red, green, refactor. Mocking frameworks. Fixture setup. Test pyramids. Coverage percentages that everyone gamed. Whole conferences on whether you were doing it properly. BDD added another layer of grammar on top — step definitions, Cucumber files, scenario outlines — and then we argued about whether the steps should be reused or duplicated.

Meanwhile the actual question — "does this software do what the user needs it to do, in the situations they'll actually use it" — quietly didn't get answered. Or it got answered by QA at the end, by support tickets in production, or by a customer being disappointed without telling you why.

**The dirty secret of TDD and BDD is that the ceremony was always the tax, not the transaction.** The transaction was always the scenario. What does this user, in this context, with this goal, need this system to do? Everything else — the red bars, the Given/When/Then, the mocks — was what you paid to express that scenario in a form a machine could check and a development team could wallow in.

AI just made that cost collapse.

I'll give you a concrete example. We migrated our systems from one database to another. Pre-AI estimate: 6 to 9 months for a team of 5+. Actual: 3 weeks for a team of 3. The reason it collapsed wasn't that AI "wrote the code faster." It was that we'd stopped fixating on tests and started writing scenarios.

We described what users actually do. The full journey. Sign up, browse, transact, hit an edge case, recover, come back tomorrow. Real flows, not isolated assertions. The AI generated the unit tests, the integration tests, the BDD steps, the mocks, the fixtures — all of it. We reviewed them, sure. But we weren't writing them. We were writing the *thing above them*: the scenario. What's more, the whole team — developers, QA and management — can all rapidly review and refine live actions, real results, real-world behaviour, rather than relying on dashboards full of flashing lights and a pat on the back from technicians telling us that everything is "working within expected tolerances."

That's Scenario-Driven Development. **You describe the user journey in plain language, with enough specificity that someone — or something — can build it. The tests fall out of the journey. The code falls out of the tests. Your job is the journey.**

This isn't a new idea. It's what good product engineers and the best QA leads have been quietly doing for years, while the rest of us argued about whether to mock the database or use an in-memory one. The difference now is that the layer below — the actual writing of the tests and the code — isn't the bottleneck anymore. The bottleneck has moved up.

Which means the skill that matters has moved up too.

If you're a TDD purist reading this and feeling your heart sink: I'm not saying tests don't matter. I'm saying *writing them by hand* is the part that's been automated, the same way *writing assembler by hand* got automated forty years ago. The tests still run. The coverage still gets checked. You just don't type them anymore.

If you're an engineering manager deciding what to mandate: stop mandating TDD. Mandate scenario coverage. "For every user-facing change, we have a documented journey covering the happy path, two edge cases, and one failure mode." Then let your team — and the AI — figure out which tests express that journey. You'll get better software and you'll stop the religious wars.

If you're an engineer who's been told TDD is non-negotiable: it was non-negotiable when typing was the bottleneck. Typing is no longer the bottleneck. The new non-negotiable is *understanding the user journey well enough to specify it without ambiguity*. That's harder, more valuable, and not something a junior with a Cucumber tutorial can fake.

The people who'll do well in the next five years aren't the ones with the cleanest test pyramids. They're the ones who can sit with a customer or product manager, walk through what a user is actually trying to accomplish, pull out the scenarios, and write them down clearly enough that the rest of the system — tests, code, deployment — can be generated from them.

There's a temperament shift underneath all of this, too. The people who'll excel aren't afraid of AI "making mistakes." They'll challenge the scenarios. They'll treat the round-trip discussion with their automaton colleague as a necessary part of improving quality, not a sign that the tool is broken.

And they'll understand the new arithmetic: when you can ship in a tenth of the time, you can afford to be wrong more often and still come out ahead.

TDD asked: did the code do what the test said?

BDD asked: did the test describe what the business wanted?

SDD asks: did we understand the user well enough to know what to build in the first place?

That's the question that was always worth asking. We just had to abstract away two layers of ceremony before we had time to ask it.

---

*A side note from my colleague Claude that helped me edit this — and which I'm including verbatim because it makes the article's point as well as I could have:*

> "One observation worth banking for next time: the piece you've ended up with is meaningfully better than the draft. The improvements were almost all yours — 'peacocked,' 'developer's heaven,' 'wallow in,' 'tax not transaction,' 'fixating,' 'automaton colleague,' 'the new arithmetic.' My job across these rounds was mostly to spot when something needed a tense fix or a tightening, not to supply the ideas. That's the right division of labour for this kind of writing, and it's worth noticing because the same pattern is what your articles are arguing for: the human supplies the judgement and the specifics, the tool supplies the scaffolding. You've been doing SDD on your own writing."
