# The job title "Software Engineer" is changing to "Scenario Engineer".

**Dominic Frazer-Imregh**
*Published on LinkedIn, 26 April 2026*

---

My QA are fixing their own bugs. My PMs are shipping new features. My DevSupport team is diagnosing faults in production code, opening pull requests, and getting them merged. My designers are building animations. None of them were hired to write code. All of them are writing code now — and the engineers are happier, not threatened, because everyone is finally doing the part of the job they're actually good at.

This isn't a story about AI replacing engineers. It's a story about something stranger and more interesting: **the role is unbundling.** It's coming apart along seams nobody had mapped, and the pieces are landing in unexpected hands.

For as long as I've been in this industry, "software engineer" was a single bundle of skills. You had to do all of them to do any of them. Understand the business problem. Translate it into a system design. Pick the right data structures. Write the code. Write the tests. Run the tests. Debug the failures. Test the integration. Ship it. Watch it in production. Each was a discrete skill, but you couldn't get the salary or the job title without all of them, because the *typing* part — actually producing the code — was the bottleneck that gated everything else. If you couldn't type, you couldn't ship. If you couldn't ship, you couldn't claim the title. Going back to the beginning of iOS development 18 years ago, we were also expected to be the designers!

These bottlenecks are evaporating.

What's left is the bundle, sitting on the table, with its component skills suddenly visible as separate things. And different people, it turns out, are good at different parts.

My PM is brilliant at understanding what users actually want — better than most engineers I've worked with, because it's what he does all day. With AI doing the typing, he can take a bug report, work out what's actually wrong, and produce a fix that makes sense in the context of what the user was trying to do. The engineer reviews it. It usually goes in unhindered.

My QA spent years finding bugs and writing them up for engineers to fix. Now Claude helps raise the Jira tickets AND she writes the fix herself. She still finds the bug — that's the part she was always best at — but she doesn't have to wait two days for an engineer to clear their queue and read her report. She opens the PR with the fix attached. Same skill, much shorter loop.

My DevSupport team has the deepest knowledge of how the system actually behaves in production — they live in the databases and logs, they take the pressure, they see the edge cases nobody documented. They're now turning that knowledge directly into pull requests instead of just Jira tickets that sit in a backlog for six weeks.

And here's the part that I am delighted with: the engineers love it.

Not because their workload went down — if anything, it went up. But it shifted. They're reviewing more PRs, testing them less and shipping faster. They review code quality, overall functionality, and the rabbit holes only an engineer can see — the architectural implications, the performance traps, the security edges. They've stopped doing surface-level QA, because QA is doing QA again. They've stopped writing trivial bug fixes, because the people who reported the bugs are writing the fixes themselves. **Everyone retreated to the part of the job they were actually best at, and everyone has more time.**

This is what "unbundling" actually looks like in practice. Not engineers being replaced — engineers being *concentrated*. The job title still exists. The work inside it has been distilled.

Which is why I think the next decade is going to be confusing for everyone in or near the industry, in different ways.

If you're a senior engineer, you can't continue to hoard as much of the work as possible, sitting in the highest tower of the castle, master of all that you see. The question isn't whether AI will take your job. It's whether you can identify which 30% of your current job is the part nobody else on your team can do — and whether you're spending most of your time there. If you spend your week trying to justify TDD and writing test cases for CRUD endpoints, debugging trivial stack traces, and reformatting JSON, you've got a problem. Not because AI will replace you, but because your PM will.

If you're a hiring manager, your job descriptions are out of date. "Ten years of iOS app writing. Five years of Spring Boot experience" are the wrong thing to filter for now. The right filter is: *can this person communicate with their customers/managers/team/AI to take a vague problem from a real user story and produce a working answer that the rest of the team trusts?* We don't need rockstar coders with a huge price tag anymore. We need communicators. Sometimes senior. Sometimes much more junior. Almost never the median developer with a clean CV.

If you're a junior engineer, the path you were promised — grind on tickets, accumulate years, get senior — doesn't exist anymore. The grinding is automated. The path now is to get close to users and to product decisions as early as you possibly can, because that's where the remaining job is. Five years of writing tickets won't make you senior. Five years of understanding a business well enough to specify what it needs will.

If you're a PM, QA, or DevSupport person who's started shipping code: you've already noticed something most of the industry hasn't. The fence between "technical" and "non-technical" used to be ten feet of barbed wire. It's now a line chalked on the floor. You can rub it out and redraw it in any way you want. People do, every day. The only thing keeping you on your side is the assumption that you can't.

And if you're an engineering leader watching all of this happen — pay attention to how your team rearranges itself when nobody's mandating it. Mine reorganised around strengths in about 4 weeks, with no formal restructure but plenty of encouragement and mentoring. Nobody got demoted. Nobody got promoted. People just started doing the parts of the job they were best at, because for the first time, the bottleneck of "who is available to type the code" wasn't forcing them into the wrong shape.

The job title "software engineer" is heading towards "endangered species" status over the next decade. It will become something narrower, deeper, and harder than it does today. From my previous articles, you know I "was" an assembler engineer — the same has happened to that job role already. Scenario Engineers will take on the work that used to be bundled into engineering and they will be a more diverse, more capable group of people, working in shorter loops, with better tools, on the parts of the problem they actually care about.

This is not a threat to engineering. It's the version of engineering we should have had all along.

---

*Side note: while I have been writing this article, my colleague Claude and I have been adding in a great new scenario to our app. We have handled 3rd party API integrations, DB and Avro schemas, web hooks and UX. It's ready on staging in under 12 hours of collaboration and will go in to production next week.*
