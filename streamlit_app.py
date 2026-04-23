import streamlit as st
from app.mcp import decide_tool, execute_tool
from app.llm import chat_with_tools
from app.database import create_table, insert_article
from app.scraper import scrape_toi

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="AI News Chatbot", page_icon="📰")
st.title("📰 AI News Chatbot")

# -------------------------
# Sidebar
# -------------------------
category = st.sidebar.selectbox(
    "Choose Category",
    ["sports", "business", "technology", "india"]
)

# -------------------------
# Load data (ONLY ONCE)
# -------------------------
@st.cache_resource
def load_data():
    create_table()
    for cat in ["sports", "business", "technology", "india"]:
        articles = scrape_toi(cat)
        for a in articles:
            insert_article(a)

load_data()

# -------------------------
# Chat memory
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Display chat history
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# Input
# -------------------------
user_input = st.chat_input("Ask latest news...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # -------------------------
    # Retrieve data
    # -------------------------
    tool = decide_tool(user_input)

    data = []
    if tool:
        data = execute_tool(tool, f"{category} {user_input}")

    # -------------------------
    # Build context
    # -------------------------
    if data:
        context = "\n\n".join(
            [f"• {d[1]}\n🔗 {d[3]}" for d in data]
        )
    else:
        # fallback → always show latest news
        fallback_data = execute_tool("get_news", category)
        context = "\n\n".join(
            [f"• {d[1]}\n🔗 {d[3]}" for d in fallback_data]
        )

    # -------------------------
    # Strict prompt
    # -------------------------
    prompt = f"""
You are a strict news assistant.

RULES:
- ONLY use the provided context
- DO NOT add external knowledge
- DO NOT explain anything
- ONLY return headlines

FORMAT:
• Headline  
🔗 Link  

Context:
{context}

User Query:
{user_input}
"""

    # -------------------------
    # LLM response
    # -------------------------
    answer = chat_with_tools(prompt)

    # Safety fallback
    if not answer or len(answer.strip()) < 20:
        answer = context

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": answer})

# -------------------------
# Clear chat
# -------------------------
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []