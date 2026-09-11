# 🧑‍💼 AI_Agents — Onboarding Packet for Your New Employee
 
Congratulations! You just hired your first **Agent**. Unlike every other session in this repo, this one doesn't just *run a chain* — it **decides what to do**. Big career jump. Let's process the paperwork.
 
---
 
## 📋 New Hire Form
 
| Field | Details |
|---|---|
| **Employee Name** | Agent (unnamed — HR is working on it) |
| **Position** | Autonomous Reasoning Unit |
| **Manager** | `create_agent()` |
| **Brain** | `gemini-3.5-flash` (temperature = 0, because this employee does not improvise) |
| **Start Date** | Immediately after `agent.invoke()` |
| **Reports To** | Whoever asks the question |
 
---
 
## 🧰 Equipment Issued
 
Every new agent gets a toolbelt on day one. Yours got two items:
 
<details>
<summary>🔍 <b>Tool #1 — DuckDuckGoSearchRun</b> (click to inspect)</summary>
A pre-built LangChain community tool. No API key drama, no rate-limit begging — just point it at a query and it goes and reads the internet for you. This is the "ask a coworker who already knows" tool.
 
</details>
<details>
<summary>🌦️ <b>Tool #2 — weather_tool</b> (click to inspect)</summary>
Custom-built, `@tool`-decorated, hits the Weatherstack API with a city name and hands back raw JSON. This is the "call the one guy who actually knows the answer" tool — except the guy is an HTTP request.
 
</details>
---
 
## 🧠 So... What Actually Happens?
 
You didn't write a script that says *"search, then get weather, then combine."* You wrote a prompt — **"capital of Rajasthan and the current weather there"** — and handed it to something that had to figure out the plan *itself*.
 
Here's the mental model, laid out as a performance review:
 
> **Task:** Find the capital of Rajasthan, then get its weather.
>
> **Step 1 — Reasoning:** "I don't know the capital for certain / need to confirm it. Let me search."
> → calls `search_tool("capital of Rajasthan")`
>
> **Step 2 — Reasoning:** "Got it — Jaipur. Now I need weather data, and I have a weather tool. Let me use it."
> → calls `weather_tool("Jaipur")`
>
> **Step 3 — Reasoning:** "I have both facts now. Time to answer the human."
> → returns final message
 
**Performance rating: ⭐⭐⭐⭐⭐** — no supervisor told it the order of operations. That ordering *emerged* from the model reasoning over which tool solves which sub-problem. This is the entire pitch of agentic AI: you stop writing the control flow, and the LLM starts writing it for you, tool call by tool call.
 
---
 
## 🔬 Guess Before You Scroll
 
What do you think `response["messages"][-1]` actually *is* by the time the agent finishes?
 
<details>
<summary>Reveal answer</summary>
It's **not just the final answer**. It's the *last message in a full conversational trail* that includes:
- your original human message
- the agent's internal tool-call requests (search, then weather)
- the tool outputs coming back in
- and finally, the agent's synthesized answer
`create_agent` runs an entire mini message-passing loop behind the scenes — think of it as the agent talking to itself (and its tools) until it's confident enough to talk to *you*.
 
</details>
---
 
## 🪪 Employee ID Card
 
```
┌─────────────────────────────────────┐
│  🆔  AGENT ID CARD                   │
│  ───────────────────────────────     │
│  Model:      gemini-3.5-flash        │
│  Tools:      2 (search, weather)     │
│  Autonomy:   Decides tool order      │
│  Temperature: 0  (no vibes, only     │
│               logic)                 │
│  Status:     ✅ Cleared for duty     │
└─────────────────────────────────────┘
```
 
---
 
## ⚠️ A Note From HR (a.k.a. a bug worth knowing)
 
`weatherstack`'s free tier serves **HTTP only**, not HTTPS — if you're using a paid key this snippet's `https://` call is fine, but on the free plan you'll need to swap to `http://` or you'll get an access-restricted error back instead of weather data. Worth remembering before your agent confidently reports "the weather is: an error message."
 
---
 
## 🚪 What's Next
 
Your agent currently has two tools and zero memory of past conversations — it's smart, but it's got amnesia. Next up: giving it something to actually **remember and retrieve from** — because an agent that can reason *and* recall is where this whole journey has been heading. RAG territory, incoming. 👀
