# Day 01 — StrOutputParser 🔗
 
## 🎯 Concept
`StrOutputParser` + Chaining prompts together (LCEL magic ✨)
 
## 🛠️ What I built
A mini pipeline:
📝 Topic → Detailed Report → 5-line Summary
(using Gemini + LangChain)
 
## 💡 Key Learnings (fun mode)
- 🍬 `StrOutputParser` = takes the AI's fancy reply object and turns it into **plain text**
- 🔗 `|` (pipe) = LEGO blocks for AI — connect prompt → model → parser → next prompt...
- 🔁 Output of one chain = input of the next chain (like a relay race 🏃‍♂️➡️🏃‍♀️)
- ⚠️ Gotcha: `input_variable` ❌ → should be `input_variables` ✅ (typo trap!)
- 🎯 `chain.invoke()` — you only feed the FIRST input, rest flows automatically
## 🧩 Code Snippet
```python
parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic": "black hole"})
```
 
## 🎉 One-liner takeaway
> Chains are just pipes passing text like a game of telephone — but smarter 😄