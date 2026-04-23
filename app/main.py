from fastapi import FastAPI
from app.llm import chat_with_tools
from app.mcp import decide_tool, execute_tool

app = FastAPI()


@app.post("/chat")
def chat(query: str, category: str = "general"):
    try:
        tool = decide_tool(query)

        data = []

        # 🔥 better query enrichment
        enhanced_query = f"{category} {query}"

        if tool:
            data = execute_tool(tool, enhanced_query)

        # build context with links
        if data:
            context = "\n".join([f"{d[1]} \n🔗 {d[3]}" for d in data])
        else:
            context = "Latest general news headlines."

        final_prompt = f"""
You are a professional news assistant.

TASK:
- Summarize news clearly
- Use bullet points
- Keep it short
- Always use given context

FORMAT:
• Headline  
🔗 Link  

Context:
{context}

User Query:
{query}
"""

        answer = chat_with_tools(final_prompt)

        # 🔥 fallback (clean)
        if not answer:
            answer = "Here are the latest headlines:\n\n" + context

        return {"response": answer}

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}