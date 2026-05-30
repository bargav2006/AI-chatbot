"""
IPL Cricket Expert Chatbot — Streamlit App
Powered by Groq API (llama-3.3-70b-versatile)
Updated: May 31, 2026 — FINAL DAY (GT vs RCB)
"""

import streamlit as st
import pandas as pd
from groq import Groq
from ipl_data import IPL_TEAMS, IPL_WINNERS, QUICK_QUESTIONS, IPL_2026_LIVE
from ipl_system_prompt import SYSTEM_PROMPT

st.set_page_config(
    page_title="IPL 2026 Cricket Expert",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&display=swap');
.match-card { background:#f8f9fa; border-radius:8px; padding:10px 14px;
    margin-bottom:8px; border-left:3px solid #f7c948; font-size:12px; }
.result-card { background:#f0fdf4; border-radius:8px; padding:10px 14px;
    margin-bottom:8px; border-left:3px solid #16a34a; font-size:12px; }
.final-card { background:#fff7ed; border-radius:8px; padding:12px 16px;
    margin-bottom:10px; border:2px solid #f59e0b; font-size:13px; text-align:center; }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_client() -> Groq:
    api_key = st.secrets.get("GROQ_API_KEY", None)
    if not api_key:
        st.error("⚠️ GROQ_API_KEY not found. Add to .streamlit/secrets.toml\nGet free: https://console.groq.com/keys")
        st.stop()
    return Groq(api_key=api_key)


for k, v in [("messages", []), ("total_tokens", 0)]:
    if k not in st.session_state:
        st.session_state[k] = v

# ── Header ─────────────────────────────────────────────────────────────────────
st.title("🏏 IPL Cricket Expert Chatbot")
st.caption("Season 19 · IPL 2026 · **FINAL DAY** — GT vs RCB | May 31, 2026")
st.divider()

main_col, side_col = st.columns([2, 1])

with side_col:

    # ── TODAY'S FINAL ─────────────────────────────────────────────────────────
    st.markdown('<div class="final-card">🏆 <b>IPL 2026 GRAND FINAL</b><br>'
                '<b style="font-size:15px">Gujarat Titans vs RCB</b><br>'
                '📅 May 31 · 7:30 PM IST<br>'
                '🏟️ Narendra Modi Stadium, Ahmedabad</div>',
                unsafe_allow_html=True)

    # ── Playoff Results ────────────────────────────────────────────────────────
    st.subheader("🏆 Playoff Results")
    for r in IPL_2026_LIVE["recent_results"][:3]:
        st.markdown(
            f'<div class="result-card">'
            f'<b>{r["match_no"]}:</b> {r["result"]}<br>'
            f'🏅 POTM: {r["potm"]}<br>'
            f'<span style="color:#666">🏟️ {r["venue"]} · {r["date"]}</span>'
            f'</div>', unsafe_allow_html=True)

    st.divider()

    # ── Points Table ──────────────────────────────────────────────────────────
    st.subheader("📊 League Stage Standings")
    st.caption("Final league table — top 4 qualified for playoffs")
    pt_data = []
    for r in IPL_2026_LIVE["points_table"]:
        status = r.get("status", "")
        flag = " ✅" if status == "Q" else (" ❌" if status == "E" else "")
        pt_data.append({"Team": r["team"] + flag, "M": r["m"],
                         "W": r["w"], "L": r["l"], "Pts": r["pts"], "NRR": r["nrr"]})
    st.dataframe(pd.DataFrame(pt_data), use_container_width=True,
                 hide_index=True, height=390)
    st.caption("✅ Qualified  ❌ Eliminated from league")

    st.divider()

    # ── Orange Cap ────────────────────────────────────────────────────────────
    st.subheader("🟠 Orange Cap")
    st.caption("After Q2 — final TBD tonight")
    oc = [{"#": i, "Player": p["name"], "Team": p["team"],
            "Runs": p["runs"], "SR": p["sr"]}
           for i, p in enumerate(IPL_2026_LIVE["orange_cap"], 1)]
    st.dataframe(pd.DataFrame(oc), use_container_width=True,
                 hide_index=True, height=290)

    st.divider()

    # ── Purple Cap ────────────────────────────────────────────────────────────
    st.subheader("🟣 Purple Cap")
    st.caption("Rabada vs Bhuvneshwar — decided tonight!")
    pc = [{"#": i, "Player": p["name"], "Team": p["team"],
            "Wkts": p["wickets"], "Econ": p["econ"]}
           for i, p in enumerate(IPL_2026_LIVE["purple_cap"], 1)]
    st.dataframe(pd.DataFrame(pc), use_container_width=True,
                 hide_index=True, height=220)

    st.divider()

    # ── Season Records ────────────────────────────────────────────────────────
    st.subheader("📊 2026 Season Records")
    for label, val in IPL_2026_LIVE["season_stats"].items():
        with st.container(border=True):
            st.caption(label)
            st.markdown(f"**{val}**")

    st.divider()

    # ── Recent match results ──────────────────────────────────────────────────
    st.subheader("🏅 Recent Results")
    for r in IPL_2026_LIVE["recent_results"][3:]:
        st.markdown(
            f'<div class="match-card">'
            f'<b>Match {r["match_no"]}:</b> {r["result"]}<br>'
            f'🏅 POTM: {r["potm"]}<br>'
            f'<span style="color:#666">🏟️ {r["venue"]} · {r["date"]}</span>'
            f'</div>', unsafe_allow_html=True)

    st.divider()
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_tokens = 0
        st.rerun()
    st.caption(f"🔢 Tokens: `{st.session_state.total_tokens:,}`")
    st.caption("Groq · llama-3.3-70b-versatile")


with main_col:
    if not st.session_state.messages:
        st.markdown("#### 💡 Quick questions:")
        cols = st.columns(2)
        for i, q in enumerate(QUICK_QUESTIONS):
            if cols[i % 2].button(q, key=f"chip_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": q})
                st.rerun()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="🏏" if msg["role"] == "assistant" else "👤"):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask about the final, playoffs, squads, stats, history..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🏏"):
            client = get_client()
            groq_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=groq_messages,
                    max_tokens=1024,
                    temperature=0.7,
                )
            answer = response.choices[0].message.content
            st.markdown(answer)
            st.session_state.total_tokens += response.usage.total_tokens

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()
