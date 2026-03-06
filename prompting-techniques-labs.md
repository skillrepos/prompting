# Prompt Engineering Accelerator — Hands-On Labs

## How to Use These Labs

Each lab is designed to take 10-12 minutes using any free AI chat interface (ChatGPT, Claude, Gemini, Copilot, or a local model via Ollama). You'll paste prompts, observe results, iterate, and compare. No coding required.

**Setup**: Open your preferred AI chat interface in a browser tab. Start a new conversation for each lab.

---

## Lab 1: Strengthen Weak Prompts (10 minutes)

**Goal**: Apply the 6 building blocks (Task, Context, Role, Format, Examples, Constraints) to transform vague prompts into structured, measurable ones.

**What you'll learn**: How adding each element systematically improves output quality, consistency, and usefulness.

### Steps

**Step 1 — Establish a baseline.** Paste this vague prompt into your AI chat and note the response:

```
Explain cloud computing.
```

Observe: How long is the response? Is it useful for any specific audience? Could you predict what format you'd get?

**Step 2 — Add a Task definition.** Now try:

```
Task: Explain the three main service models of cloud computing (IaaS, PaaS, SaaS).
```

Compare: Is the output more focused? Does it cover what you expected?

**Step 3 — Add Context and Audience.** Build on the prompt:

```
Task: Explain the three main service models of cloud computing (IaaS, PaaS, SaaS).
Context: The audience is a group of small business owners evaluating whether to migrate from on-premises servers. They have no technical background.
```

Compare: Has the language changed? Are the explanations more relevant to the audience?

**Step 4 — Add a Role.** Add a persona:

```
Role: You are a cloud computing consultant who specializes in helping small businesses migrate to the cloud. You explain technical concepts using everyday business analogies.

Task: Explain the three main service models of cloud computing (IaaS, PaaS, SaaS).
Context: The audience is a group of small business owners evaluating whether to migrate from on-premises servers. They have no technical background.
```

Compare: Do you notice analogies or a different communication style?

**Step 5 — Add Format requirements.** Specify the output structure:

```
Role: You are a cloud computing consultant who specializes in helping small businesses migrate to the cloud. You explain technical concepts using everyday business analogies.

Task: Explain the three main service models of cloud computing (IaaS, PaaS, SaaS).
Context: The audience is a group of small business owners evaluating whether to migrate from on-premises servers. They have no technical background.

Format: For each service model, provide:
- Name and one-sentence definition
- A real-world business analogy
- One example use case for a small business
- Estimated monthly cost range

Present as a comparison table.
```

Compare: Is the output now consistently structured and easy to scan?

**Step 6 — Add Constraints.** Add boundaries:

```
Role: You are a cloud computing consultant who specializes in helping small businesses migrate to the cloud. You explain technical concepts using everyday business analogies.

Task: Explain the three main service models of cloud computing (IaaS, PaaS, SaaS).
Context: The audience is a group of small business owners evaluating whether to migrate from on-premises servers. They have no technical background.

Format: For each service model, provide:
- Name and one-sentence definition
- A real-world business analogy
- One example use case for a small business
- Estimated monthly cost range

Present as a comparison table.

Constraints:
- No jargon without immediate explanation
- Keep total response under 300 words
- End with a one-sentence recommendation for a typical 10-person office
```

**Step 7 — Run the final prompt 3 times.** Paste the complete prompt from Step 6 three separate times (in new conversations or after clearing context). Compare the three outputs:
- Do they all follow the table format?
- Are the analogies consistent in quality?
- Does the recommendation stay relevant?

This is measuring **consistency** — a key quality metric.

**Step 8 — Reflect.** Rate each version (Steps 1-6) on a 1-5 scale for: specificity, usefulness, and consistency. Note which building block made the biggest difference for this task.

---

## Lab 2: Few-Shot & Chain of Thought Comparison (12 minutes)

**Goal**: Compare zero-shot, few-shot, and Chain of Thought (CoT) prompting on a support ticket priority task where the "correct" answer depends on company-specific rules that only examples can teach.

**What you'll learn**: How few-shot examples encode domain-specific policies that zero-shot can't infer from category names alone, and how CoT makes classification decisions auditable and debuggable.

### Steps

**Step 1 — Zero-shot priority classification.** Paste this prompt and record the AI's answer:

```
You are a support ticket classifier. Assign exactly one priority level to the following support ticket: P1-Critical, P2-High, P3-Medium, or P4-Low.

Ticket: "Hi, just a heads-up — I noticed some of my files from last Tuesday seem to be missing from the shared drive. Not urgent, but could someone take a look when they get a chance? Thanks!"
```

Record the priority assigned. The ticket is politely worded and the customer explicitly says "not urgent" — the AI will likely follow the customer's lead. But should it? (Hint: the ticket describes *data loss*.)

**Step 2 — Test with more tickets.** Classify these one at a time using the same zero-shot prompt (just change the ticket). Record each result:

```
Ticket: "THIS IS UNACCEPTABLE. I updated my profile photo and it's been 3 hours and the old one still shows on some pages. Fix this NOW or I'm switching to a competitor. WORST. SERVICE. EVER."
```
```
Ticket: "We're evaluating your platform for a potential 500-seat enterprise deployment. Could you help us understand your SSO integration options?"
```
```
Ticket: "The export button on the reports page gives a 404 error. I can work around it by using the API, but figured you'd want to know."
```
```
Ticket: "Our team of 12 can't access the platform at all since this morning. We have client deliverables due today."
```

Before looking at results, write down what YOU would assign to each. Then compare.

**Step 3 — Examine the zero-shot results.** Zero-shot classifies based on tone, urgency language, and apparent severity. But companies often have specific priority policies that override surface signals. Consider:
- The polite "missing files" ticket (Step 1): Zero-shot probably assigned P3 or P4 because the customer said "not urgent." But data loss is *always* critical in most support policies, regardless of how the customer phrases it.
- The angry profile photo ticket: Zero-shot probably assigned P2 or P3 because of the furious tone. But a profile photo cache delay is a P4-Low cosmetic issue — the anger is wildly disproportionate to the actual problem.
- The "evaluating for 500-seat deployment" ticket: Zero-shot might assign P3 or P4 since it's just a question. But a potential enterprise deal is a high-priority revenue opportunity.

Note which tickets the AI classified based on *tone* rather than *business impact*.

**Step 4 — Now try few-shot prompting.** Provide examples that encode specific priority rules:

```
You are a support ticket classifier. Assign exactly one priority level: P1-Critical, P2-High, P3-Medium, or P4-Low.

Company priority rules (taught by example):

Ticket: "I accidentally deleted some records from the database and can't find them in the trash."
Priority: P1-Critical
(Data loss or potential data loss is always P1, regardless of customer tone.)

Ticket: "YOUR APP IS THE WORST THING I'VE EVER USED. The font size on the settings page is too small to read."
Priority: P4-Low
(Cosmetic/UI preference issues are P4 regardless of how angry the customer is.)

Ticket: "We're a 200-person company looking at your enterprise plan. Can someone walk us through pricing?"
Priority: P2-High
(Pre-sales inquiries from potential enterprise customers are P2 — revenue opportunity.)

Ticket: "None of our team members can log in. Affecting 30+ users since 9 AM."
Priority: P1-Critical
(Service outages affecting multiple users are always P1.)

Ticket: "The CSV export includes an extra blank column at the end. Minor annoyance but thought you should know."
Priority: P3-Medium
(Functional bugs with easy workarounds are P3.)

Ticket: "I've been on hold for 45 minutes and I'm FURIOUS. I just need to update my billing address."
Priority: P4-Low
(Routine account changes are P4 regardless of customer frustration with wait times.)

Now classify this ticket:
Ticket: "Hi, just a heads-up — I noticed some of my files from last Tuesday seem to be missing from the shared drive. Not urgent, but could someone take a look when they get a chance? Thanks!"
```

Notice the key policy encoded in these examples: **priority is based on business impact, not customer tone.** Angry customers with minor issues get P4. Polite customers reporting data loss get P1.

**Step 5 — Classify all test tickets with few-shot.** Run each of the 4 test tickets from Step 2 through your few-shot prompt. Record results side by side with zero-shot.

**Step 6 — Compare zero-shot vs. few-shot.** Look at where the results differ:
- Did the "missing files" ticket get upgraded from P3/P4 to P1? (The examples teach that data loss = P1 regardless of tone.)
- Did the angry profile photo ticket get downgraded to P4? (The examples teach that cosmetic issues are P4 regardless of how furious the customer is.)
- Did the "500-seat evaluation" ticket get upgraded to P2? (The examples teach that enterprise pre-sales = high priority.)
- How many tickets changed classification? This is the power of few-shot: it teaches business rules the model can't infer from category names alone.

**Step 7 — Add Chain of Thought.** Now add structured reasoning before classification:

```
You are a support ticket classifier. Assign exactly one priority level: P1-Critical, P2-High, P3-Medium, or P4-Low.

Before classifying, reason through these steps:
1. What is the actual technical/business issue? (Ignore emotional language — focus on what's broken or needed.)
2. What is the blast radius? (One user, a team, all users, or a potential customer?)
3. Is there data loss, a security risk, or a revenue impact?
4. Does the customer have a workaround?
5. Based on business impact (not tone), assign priority.

Examples:

Ticket: "I accidentally deleted some records from the database and can't find them in the trash."
Reasoning:
1. Issue: Data has been deleted and cannot be recovered through normal means.
2. Blast radius: At minimum one user's data; could affect shared records.
3. Data loss: Yes — confirmed missing records with no recovery path.
4. Workaround: None apparent — data is gone.
5. Data loss with no workaround is always critical.
Priority: P1-Critical

Ticket: "YOUR APP IS THE WORST THING I'VE EVER USED. The font size on the settings page is too small to read."
Reasoning:
1. Issue: Font size on one page is too small. This is a UI/cosmetic preference.
2. Blast radius: One user's visual preference; settings page is rarely visited.
3. Data loss/security/revenue: None.
4. Workaround: Browser zoom, accessibility settings.
5. Cosmetic issue with available workarounds, despite angry tone.
Priority: P4-Low

Now classify:
Ticket: "Hi, just a heads-up — I noticed some of my files from last Tuesday seem to be missing from the shared drive. Not urgent, but could someone take a look when they get a chance? Thanks!"
```

**Step 8 — Test CoT on all tickets.** Run each test ticket through the CoT prompt. Record the results.

**Step 9 — Build a comparison table.** Create a simple table:

| Ticket (short) | Zero-Shot | Few-Shot | CoT | Correct |
|----------------|-----------|----------|-----|---------|
| Missing files (polite) | | | | P1 |
| Profile photo (angry) | | | | P4 |
| 500-seat evaluation | | | | P2 |
| Export 404 (workaround) | | | | P3 |
| Team of 12 locked out | | | | P1 |

Fill in all results. The "Correct" column reflects the company's policy: priority by business impact, not customer tone. How did each technique score?

**Step 10 — Evaluate and reflect.** Consider what you observed:
- **Zero-shot** likely followed customer tone: angry customers got high priority, polite customers got low priority. How many did it get "wrong" by the company's actual policy?
- **Few-shot** encoded the "impact over tone" rule through examples. Did it correctly override tone-based classification? Which tickets flipped to the right answer?
- **CoT** made the reasoning visible. For the polite "missing files" ticket, did the reasoning chain correctly identify data loss as the key factor despite the casual tone? Could you hand this reasoning to a manager to explain why a "not urgent" ticket was classified P1?

Key takeaway: few-shot is most powerful when the correct classification depends on **domain-specific rules** that contradict the model's general intuition. CoT adds value when you need to **audit and explain** why a non-obvious classification was made.

---

## Lab 3: Production Prompt Engineering (12 minutes)

**Goal**: Build a structured, constrained prompt that produces consistent JSON output suitable for integration into a real system — and see exactly where unstructured prompts break down.

**What you'll learn**: How to combine role, structure, constraints, and format specifications to create production-grade prompts. Why "it mostly works" isn't good enough for systems that consume AI output.

### Steps

**Step 1 — Expose the inconsistency of loose prompts.** Paste this prompt to document a user registration endpoint:

```
Write an API documentation entry for a user registration endpoint.
```

Now, **in a new conversation**, paste this for a different endpoint:

```
Write an API documentation entry for a password reset endpoint.
```

Compare the two outputs side by side:
- Did they use the same format? (Probably not — one might be markdown, the other prose, another might use tables.)
- Did they cover the same fields? (One might mention error codes, the other might skip them.)
- Could a script parse both outputs the same way? (Almost certainly not.)

This is the core problem: without structure, every output is a snowflake.

**Step 2 — Define structured JSON output.** Now specify exactly what you want:

```
Task: Generate API documentation for a REST endpoint.

Output as JSON with exactly this schema:
{
  "endpoint": "/path",
  "method": "GET|POST|PUT|DELETE",
  "description": "One sentence describing what this endpoint does",
  "parameters": [
    {
      "name": "param_name",
      "type": "string|integer|boolean|object",
      "required": true|false,
      "description": "What this parameter does"
    }
  ],
  "response": {
    "status_code": 200,
    "body": { "example": "response" }
  },
  "errors": [
    { "status_code": 400, "message": "Error description" }
  ]
}

Document this endpoint: User Registration - creates a new user account with email and password.
```

**Step 3 — Validate the output.** Check the JSON response:
- Is it valid JSON? (Copy it into jsonlint.com or any JSON validator.)
- Does it match the schema exactly?
- Are all fields present?

Now run it for the password reset endpoint too. Are both outputs structurally identical? This is the improvement — but we're not done.

**Step 4 — Find what the schema alone doesn't control.** Look closely at your Step 2 outputs:
- Are the descriptions a consistent length, or is one a sentence and another a paragraph?
- Are the parameter names formatted consistently (snake_case, camelCase, or mixed)?
- Is the example response data realistic ("john@email.com") or generic ("string", "example")?
- How many error cases did it include — 1? 3? 5?

The schema controls *structure* but not *quality*. That's what constraints are for.

**Step 5 — Add role and constraints for quality.** Enhance the prompt:

```
Role: You are a senior API technical writer who produces documentation that passes automated schema validation. You prioritize accuracy and completeness over brevity.

Task: Generate API documentation for a REST endpoint.

Output as JSON with exactly this schema:
{
  "endpoint": "/path",
  "method": "GET|POST|PUT|DELETE",
  "description": "One sentence, max 20 words, starting with a verb",
  "parameters": [
    {
      "name": "param_name (snake_case only)",
      "type": "string|integer|boolean|object",
      "required": true|false,
      "description": "Max 15 words"
    }
  ],
  "response": {
    "status_code": 200,
    "body": { "realistic_example": "with actual sample data" }
  },
  "errors": [
    { "status_code": 400, "message": "Specific, actionable error message" }
  ],
  "authentication": "none|api_key|bearer_token|oauth2",
  "rate_limit": "requests per minute"
}

Constraints:
- Output ONLY valid JSON, no markdown formatting, no explanation before or after
- Include at least 3 error cases
- All example data must be realistic (no "example" or "test" placeholders)
- Parameter names must use snake_case

Document this endpoint: User Registration - creates a new user account with email, password, and optional display name.
```

**Step 6 — Compare Step 2 vs. Step 5.** Run the constrained prompt for both endpoints (registration and password reset). Now compare against your Step 2 outputs:
- Are descriptions now consistently concise (under 20 words, starting with a verb)?
- Are parameter names all snake_case?
- Do you get exactly 3+ error cases every time?
- Is the example data realistic instead of placeholder text?

The constraints closed the quality gaps that the schema alone left open.

**Step 7 — Stress-test with a complex endpoint.** Test with:

```
Document this endpoint: Search Products - searches the product catalog by keyword with pagination and filtering by category and price range.
```

This endpoint has many more parameters. Does the prompt handle the increased complexity correctly? Are all the constraint rules still followed?

**Step 8 — Stress-test with a minimal endpoint.** Now try the opposite extreme:

```
Document this endpoint: Health Check - returns server status (no parameters needed).
```

Does the prompt handle a zero-parameter endpoint gracefully, or does it hallucinate unnecessary parameters? If it does, how would you modify the prompt to handle this? (Hint: you could add a constraint like "If the endpoint has no parameters, use an empty array.")

**Step 9 — Build your validation checklist.** Based on everything you've seen, write a checklist you could hand to a colleague (or encode in a script) to validate any output:
1. Valid JSON that parses without errors?
2. All required fields present with correct types?
3. Descriptions within word limits and starting with a verb?
4. At least 3 error cases with specific messages?
5. Realistic sample data (no "example", "test", or "string" placeholders)?
6. Parameter names consistently snake_case?

**Step 10 — Reflect.** You've built three versions: loose (Step 1), schema-only (Step 2), and schema + constraints (Step 5). The progression shows three distinct levels of production readiness:
- **Loose**: Human-readable but unparseable and inconsistent
- **Schema-only**: Parseable and structured but with uncontrolled quality variation
- **Schema + constraints**: Parseable, structured, AND consistently high quality

Which version could you hand off to a developer to integrate into a pipeline? That's the bar for "production-ready."

---

## Lab 4: Multi-Expert & Reverse Prompting (12 minutes)

**Goal**: Use multi-expert prompting to get diverse perspectives on a complex decision, then use reverse prompting to discover hidden requirements.

**What you'll learn**: How simulating multiple expert viewpoints catches blind spots, and how letting the AI ask questions produces better specifications.

### Steps

**Step 1 — Single-perspective baseline.** Paste this prompt:

```
Should our company adopt a 4-day work week? Give your recommendation.
```

Note the response: Does it consider multiple angles or lean toward one perspective?

**Step 2 — Multi-expert panel.** Now simulate a panel of experts:

```
Task: Analyze whether a 200-person software company should adopt a 4-day work week.

Simulate a panel of 4 experts. Each expert must provide their analysis independently:

Expert 1 - HR Director (15 years experience):
Focus on: employee retention, recruitment advantage, burnout, morale
Provide: Assessment + specific risk + specific benefit

Expert 2 - CFO:
Focus on: productivity impact, revenue implications, operational costs, client coverage
Provide: Assessment + financial estimate + key assumption

Expert 3 - Engineering Manager:
Focus on: sprint velocity, code quality, collaboration time, deep work
Provide: Assessment + metric prediction + mitigation strategy

Expert 4 - Employment Lawyer:
Focus on: labor law compliance, contract modifications, overtime implications, precedent cases
Provide: Assessment + top legal risk + required action

After all 4 experts present, provide:
- Points of agreement across experts
- Points of conflict between experts
- A synthesis recommendation with confidence level (low/medium/high)
- The single most important factor the decision hinges on
```

**Step 3 — Compare depth.** Compare the Step 1 and Step 2 responses:
- How many distinct perspectives were covered in each?
- Did the multi-expert version surface risks you hadn't considered?
- Was the synthesis recommendation more nuanced?

**Step 4 — Customize the panel.** Choose a decision relevant to your own work (e.g., adopting a new tool, changing a process, launching a feature). Modify the expert panel to include 3-4 roles relevant to that decision. Run it.

**Step 5 — Transition to reverse prompting.** Now let's flip the script. Instead of you writing the prompt, let the AI ask the questions. Paste:

```
I want to write a prompt that generates a comprehensive project proposal for a software project. But instead of me writing that prompt, I want you to help me discover what the prompt needs.

Ask me a series of clarifying questions — one at a time — to understand:
- What kind of project this is for
- Who will read the proposal
- What sections are required
- What constraints exist
- What level of detail is needed

Ask your first question now. After I answer each question, ask the next one. After 5-6 questions, generate the complete prompt for me.
```

**Step 6 — Answer the AI's questions.** Respond to each question the AI asks. Be as specific or vague as you'd naturally be — this tests whether the AI asks good follow-ups. Go through 5-6 rounds of questions.

**Step 7 — Evaluate the generated prompt.** After the AI generates your prompt, assess it:
- Did it capture details you wouldn't have included on your own?
- Is it more specific than what you would have written from scratch?
- Does it include elements from the 6 building blocks?

**Step 8 — Test the generated prompt.** Take the prompt the AI created and use it in a new conversation. Does the output match what you envisioned?

**Step 9 — Compare approaches.** Think about what each technique revealed:
- Multi-expert: How many distinct risks and perspectives did it surface vs. Step 1's single-perspective answer? Count them.
- Reverse prompting: Did the AI ask you about things you hadn't considered? List 2-3 details the generated prompt included that you wouldn't have thought of on your own.

**Step 10 — Reflect on when to use each.** These techniques solve different problems:
- **Multi-expert** is best when you already know the question but need to stress-test it from multiple angles. Use it for decisions with competing stakeholder interests.
- **Reverse prompting** is best when you don't know what you don't know — when the problem space is unfamiliar or you suspect you're missing requirements.
- **Combined**: In practice, you'd use reverse prompting first (to discover requirements), then feed those into a multi-expert analysis (to stress-test the decision). Write down one real decision at work where this two-step approach would be valuable.

---

## Lab 5: Optimization & Integration (10 minutes)

**Goal**: Apply probabilistic prompting and incentive framing to maximize quality on a high-stakes task, then build a reusable decision-making template.

**What you'll learn**: How multi-round self-critique and audience framing each independently improve output quality — and how combining them produces the most reliable results.

### Steps

**Step 1 — Baseline decision analysis.** Paste this straightforward prompt:

```
Task: Recommend a database for a new e-commerce application that expects 10,000 daily active users, needs to store product catalogs, user profiles, and order history.

Options: PostgreSQL, MongoDB, DynamoDB

Which should we choose and why?
```

Read the response and note:
- Does it acknowledge trade-offs, or just advocate for one option?
- Does it mention any uncertainty or risks?
- Does it consider what might change in the future?

**Step 2 — Add multi-round self-critique.** Use the exact same task and context, but change the analysis structure:

```
Task: Recommend a database for a new e-commerce application that expects 10,000 daily active users, needs to store product catalogs, user profiles, and order history.

Options: PostgreSQL, MongoDB, DynamoDB

Provide your analysis in 3 rounds:

Round 1 - Initial assessment: Rate each option from 1-10 for fit, with a one-sentence justification for each.

Round 2 - Devil's advocate: For your top-rated option, list the 3 strongest arguments AGAINST choosing it. Re-rate all options after considering these counter-arguments.

Round 3 - Final recommendation: State your recommended choice with a confidence level (0-100%). Explain what would need to be true for your second-choice option to become the better pick.
```

**Step 3 — Compare Step 1 vs. Step 2.** The task and context are identical — the only difference is the multi-round structure. Compare:
- Did the Round 2 devil's advocate surface risks that Step 1 ignored?
- Did the ratings change between Round 1 and Round 2? (If so, the self-critique actually worked.)
- Did the confidence percentage help you gauge how certain the recommendation really is?
- Did the "what would need to be true" condition give you a concrete revisit trigger?

This is the value of **probabilistic prompting**: forcing the model to argue against its own first instinct.

**Step 4 — Isolate the effect of incentive framing.** Now take your Step 2 prompt and add ONLY an audience frame at the top. Keep everything else identical:

```
This analysis will be presented to the CTO and VP of Engineering for a final architecture decision. The chosen database will serve as our primary data store for the next 3-5 years, so accuracy and completeness are critical.

Take your time and be thorough. Consider edge cases and failure modes that are easy to overlook.

Task: Recommend a database for a new e-commerce application that expects 10,000 daily active users, needs to store product catalogs, user profiles, and order history.

Options: PostgreSQL, MongoDB, DynamoDB

Provide your analysis in 3 rounds:

Round 1 - Initial assessment: Rate each option from 1-10 for fit, with a one-sentence justification for each.

Round 2 - Devil's advocate: For your top-rated option, list the 3 strongest arguments AGAINST choosing it. Re-rate all options after considering these counter-arguments.

Round 3 - Final recommendation: State your recommended choice with a confidence level (0-100%). Explain what would need to be true for your second-choice option to become the better pick.
```

**Step 5 — Compare Step 2 vs. Step 4.** The ONLY change was adding the incentive frame. Look for:
- Are the justifications longer or more detailed?
- Did it mention additional risk factors or edge cases?
- Is the language more precise (specific numbers, concrete scenarios vs. vague generalities)?
- Did the confidence percentage change?

This isolates the effect of **incentive framing** — telling the model who the audience is and that the stakes are high.

**Step 6 — Build your reusable template.** Now combine everything that worked into a general-purpose decision template:

```
[INCENTIVE FRAME]
This analysis will inform a critical decision for [stakeholder].
Accuracy and completeness are essential. Take your time.

[CONTEXT]
Decision: [What we're deciding]
Options: [Option A, Option B, Option C]
Current situation: [Key constraints and requirements]
Timeline: [When decision is needed and implementation horizon]

[MULTI-ROUND ANALYSIS]
Round 1: Rate each option (1-10) with one-line justification.
Round 2: For the top option, list 3 strongest counter-arguments. Re-rate.
Round 3: Final recommendation with:
- Confidence level (0-100%)
- Biggest risk of recommended option
- What would change your recommendation
- Revisit trigger for 6-month check-in

[FORMAT]
Present as structured sections with clear headers.
Keep total response under 500 words.
```

**Step 7 — Test your template on a real decision.** Apply your template to a decision you're actually facing — choosing a tool, vendor, approach, or process change. Fill in the brackets and run it. Does the output feel decision-ready?

**Step 8 — Final reflection.** Across all five labs, you've built a toolkit:
- Lab 1: The 6 building blocks for constructing any prompt
- Lab 2: Few-shot and CoT for accuracy on nuanced tasks
- Lab 3: Structured outputs + constraints for production systems
- Lab 4: Multi-expert and reverse prompting for complex decisions
- Lab 5: Self-critique + incentive framing for high-stakes quality

Write down the one technique you'll use first thing tomorrow — and what task you'll apply it to.

---

## Appendix: Quick Reference Card

### The 6 Building Blocks
1. **Task** — One clear, testable instruction
2. **Context** — Background, audience, environment
3. **Role** — Persona with relevant expertise
4. **Format** — Output structure (table, JSON, bullets)
5. **Examples** — Input/output pairs (few-shot)
6. **Constraints** — Boundaries (length, tone, exclusions)

### Technique Selection Guide

| Situation | Technique | Why |
|-----------|-----------|-----|
| Simple, common task | Zero-shot | Fast, low cost |
| Need consistent format | Few-shot | Examples anchor structure |
| Complex reasoning | Chain of Thought | 20-40% accuracy boost |
| Multi-stakeholder decision | Multi-expert | Catches blind spots |
| Unclear requirements | Reverse prompting | AI discovers what you need |
| High-stakes output | Probabilistic + incentive | Maximum thoroughness |
| Production integration | Structured + constrained | Consistent, parseable output |

### Quality Metrics Checklist
- Does the output follow the requested format?
- Is it consistent across multiple runs?
- Is the content accurate and grounded?
- Could downstream systems parse it reliably?
- Would a domain expert approve the output?

---
*© 2026 Tech Skills Transformations*

