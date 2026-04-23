import streamlit as st
import requests

# Page config
st.set_page_config(page_title="AI News Chatbot", page_icon="📰")

# Header
st.image("https://cdn-icons-png.flaticon.com/512/21/21601.png", width=80)
st.title("📰 AI News Chatbot")

st.sidebar.title("Categories")
category = st.sidebar.selectbox("Choose", ["sports", "business", "technology", "india"])

st.markdown("---")

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🤖" if msg["role"]=="assistant" else "🧑"):
        st.markdown(msg["content"], unsafe_allow_html=True)

# Input
user_input = st.chat_input("Ask about latest news...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    # Call backend with loading
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Fetching latest news... ⏳"):
            try:
                response = requests.post(
    "http://127.0.0.1:8000/chat",
    params={
        "query": user_input,
        "category": category   # ✅ ADD THIS LINE
    },
    timeout=10
)

                data = response.json()

                bot_reply = data.get("response", "⚠️ Error: No response")

            except Exception as e:
                bot_reply = "⚠️ Backend not running or error occurred."

        # Display response
        st.markdown(bot_reply, unsafe_allow_html=True)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []