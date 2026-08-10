# Claude told me 42. I never asked the question.

**Dominic Frazer-Imregh**
*Published on LinkedIn, 6 May 2026*

---

A civilisation builds the second-greatest computer ever conceived. They ask it the Ultimate Question of Life, the Universe, and Everything. It thinks for seven and a half million years. It returns the answer: forty-two. Everyone is annoyed. Deep Thought, slightly defensive, points out that the problem is they never properly understood the question. They commission a much bigger computer to work out what the question actually was. That computer is Earth.

Note that this is funny when Douglas Adams writes it. It's slightly less funny when it's happening to you on a Tuesday afternoon.

A few weeks ago our staging servers were struggling intensely with our increased testing. This had been "resolved" by devops a long time ago, but never really resolved. I asked Claude to look at it. Claude looked. Claude found the problem: the CPU allocation was set to 3%, causing pods to run out of resources really quickly, attempt to scale up to the max and then sit there and hope. It suggested a fix. We applied the fix. The system got faster. I moved on.

That's the whole story. Total elapsed time from problem to fix: short enough that I didn't think about it again until I sat down to write this and not long enough to make a cup of "brownian motion".

Three days later, I caught myself thinking: why was 3% wrong? Was it 3% of a node? 3% of the request limit? 3% of what we'd had before? Why was 50% the right answer? Why not 30%, or 80%? I never asked. Claude suggested 50%; we did it; the symptoms went away; case closed for now.

If an engineer on my team had brought me that fix without explaining the why, we'd at least have tried it out as an experiment — talked through what we expected to happen, what we'd watch for, how we'd know if it was right. That's how engineering teams handle uncertain fixes. Claude got none of that scrutiny. We sort of trusted it and just shipped.

Deep Thought's descendants spent generations regretting that they'd accepted the answer without preserving the question. They built a planet to recover it. We just close the ticket and move on. Same problem. Different time horizon. The 42 we're given by AI is correct enough, often enough, that we stop asking what the question was — and that's the moment the work becomes unrepeatable, undefensible, and slowly, invisibly, not really yours.

It's not that I think AI shouldn't have given me the answer. It's that I could have asked the next question, and I didn't. The tool is faster than my curiosity now and it takes short cuts, choosing the quicker/shorter answer. The fix was actually correct. The exact understanding was missing. And in a profession where understanding is the value — where the actual product of senior engineering is judgement, traceable reasoning, the ability to defend a decision under pressure — shipping a fix you can't defend is a slow transfer of responsibility for the thing you were hired for.

I notice this most in two places: bug fixes (where I know what the symptom was, but not necessarily why the proposed cause was the cause — especially with SpringBoot which is not my speciality) and reports (where I have a finding, but not the full chain of evidence that produced it). Both are versions of the same problem. Both are 42-shaped. Both are easier to live with than they should be.

What I've started doing — and this is genuinely a working note, not a prescription — is asking one extra question after every Claude answer. Not "are you sure?" That's worthless; it'll be sure if it isn't. The question is: "what would have to be true for this answer to be wrong?" Or: "what was the second-best fix you considered, and why did you reject it?" Or, simplest: "what's the question this answer is the answer to?"

The answers to those questions are sometimes more useful than the original answer was. Sometimes they reveal that I was asking the wrong thing in the first place. Sometimes they reveal that Claude's confidence was real but narrow — the fix worked for this configuration but would have failed if a load profile shifted next week. Mostly they reveal nothing new and I move on faster.

But every time I ask, I'm closer to being able to defend the answer to a teammate, a board, or a future version of myself who's debugging the same thing in eighteen months and can't remember why we did this.

Deep Thought was right. The answer was 42. The problem was that nobody knew what the question had been. We are now living in a moment where the answers are arriving faster than the questions can keep up, and the temptation is to take the answer and move on.

I'd resist that temptation, gently. Not because the AI is wrong. Because I am.
