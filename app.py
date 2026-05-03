import streamlit as st
import time

from llm import call_llm
from agent import Agent
from engine import DebateEngine

st.set_page_config(page_title="AI Debate Arena", layout="wide")

st.title("🧠 AI Debate System")

topic = st.text_input("Enter debate topic:")
rounds = st.slider("Rounds", 1, 5, 2)

start = st.button("Start Debate")

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# AGENT COLORS
# -----------------------------
AGENT_STYLES = {
    "Alex": "#ff4d4d",     # red (skeptic)
    "Bella": "#2ecc71",    # green (optimist)
    "Chris": "#3498db"     # blue (analyst)
}

# -----------------------------
# RUN DEBATE
# -----------------------------
if start and topic:

    st.session_state.messages = []

    agents = [
        Agent("Alex", "logical skeptic", call_llm),
        Agent("Bella", "optimist", call_llm),
        Agent("Chris", "data analyst", call_llm)
    ]

    engine = DebateEngine(agents)

    chat_box = st.empty()

    result = engine.run(topic, rounds)

    for msg in result:

        speaker = msg.split(":")[0] if ":" in msg else "Agent"

        # -------------------------
        # TYPING INDICATOR
        # -------------------------
        chat_box.markdown(
            f"🟡 **{speaker} is typing...**"
        )
        time.sleep(0.6)

        # -------------------------
        # ADD MESSAGE
        # -------------------------
        st.session_state.messages.append(msg)

        # -------------------------
        # RENDER CHAT (COLORED UI)
        # -------------------------
        rendered = []

        for m in st.session_state.messages:

            sp = m.split(":")[0] if ":" in m else "Agent"
            color = AGENT_STYLES.get(sp, "#ffffff")

            text = m.split(":", 1)[1] if ":" in m else m

            rendered.append(f"""
<div style="
    padding:10px;
    margin:8px 0;
    border-radius:10px;
    background-color:#1e1e1e;
    border-left:5px solid {color};
">

<b style="color:{color}; font-size:16px;">
{sp}
</b><br>

<span style="color:#e0e0e0;">
{text}
</span>

</div>
""")

        chat_box.markdown("".join(rendered), unsafe_allow_html=True)

        time.sleep(0.3)

# -----------------------------
# FINAL MESSAGE
# -----------------------------
if start and topic:
    st.success("Debate Completed ")