"""
IPL Cricket Expert Chatbot — Streamlit App
Powered by Groq API (llama-3.3-70b-versatile)
Updated: June 1, 2026 — IPL 2026 COMPLETE. RCB won back-to-back!
"""

import streamlit as st
import pandas as pd
from groq import Groq
from ipl_data import IPL_TEAMS, IPL_WINNERS, QUICK_QUESTIONS, IPL_2026_LIVE
from ipl_system_prompt import SYSTEM_PROMPT

st.set_page_config(
    page_title="IPL Cricket Expert Chatbot",
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
.champion-banner { background:linear-gradient(135deg,#1a1a2e,#16213e);
    border-radius:12px; padding:16px 20px; margin-bottom:12px;
    border:2px solid #f7c948; text-align:center; }
.award-card { background:#fffbeb; border-radius:8px; padding:8px 12px;
    margin-bottom:6px; border-left:3px solid #f59e0b; font-size:12px; }
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

st.title("🏏 IPL Cricket Expert Chatbot")
st.caption("Season 19 · IPL 2026 COMPLETE · **RCB are back-to-back champions!** 🏆🏆")
st.divider()

main_col, side_col = st.columns([2, 1])

with side_col:

    # Champion banner
    st.markdown("""
    <div class="champion-banner">
        <div style="color:#f7c948;font-family:Rajdhani,sans-serif;font-size:18px;font-weight:700">
            🏆 IPL 2026 CHAMPIONS
        </div>
        <div style="color:white;font-size:20px;font-weight:700;margin:4px 0">
            Royal Challengers Bengaluru
        </div>
        <div style="color:rgba(255,255,255,0.7);font-size:12px">
            Beat GT by 5 wkts | Kohli 75*(42) | May 31, Ahmedabad
        </div>
        <div style="color:#f7c948;font-size:11px;margin-top:4px">
            Back-to-back titles 🏆🏆 | Only 3rd team ever!
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Final scorecard
    st.subheader("🏏 Final Scorecard")
    sc = IPL_2026_LIVE["final_scorecard"]
    with st.container(border=True):
        st.markdown(f"**GT:** {sc['GT_innings']}")
        st.markdown(f"**RCB:** {sc['RCB_innings']}")
        st.markdown(f"**Result:** {sc['result']}")
        st.caption(f"📅 {sc['date']} · 🏟️ {sc['venue']}")

    st.divider()

    # All season awards
    st.subheader("🎖️ IPL 2026 Awards")
    for label, val in IPL_2026_LIVE["season_stats"].items():
        st.markdown(
            f'<div class="award-card"><span style="font-size:11px;color:#666">{label}</span><br>'
            f'<span style="font-weight:700">{val}</span></div>',
            unsafe_allow_html=True)

    st.divider()

    # Points Table
    st.subheader("📊 Final League Table")
    pt_data = []
    for r in IPL_2026_LIVE["points_table"]:
        flag = " ✅" if r.get("status") == "Q" else (" ❌" if r.get("status") == "E" else "")
        pt_data.append({"Team": r["team"] + flag, "M": r["m"],
                        "W": r["w"], "L": r["l"], "Pts": r["pts"], "NRR": r["nrr"]})
    st.dataframe(pd.DataFrame(pt_data), use_container_width=True,
                 hide_index=True, height=390)
    st.caption("✅ Qualified for playoffs  ❌ Eliminated in league")

    st.divider()

    # Orange Cap
    st.subheader("🟠 Orange Cap — Final")
    oc = [{"#": i, "Player": p["name"], "Team": p["team"],
            "Runs": p["runs"], "SR": p["sr"]}
           for i, p in enumerate(IPL_2026_LIVE["orange_cap"], 1)]
    st.dataframe(pd.DataFrame(oc), use_container_width=True,
                 hide_index=True, height=290)
    st.caption("🏅 Winner: Vaibhav Sooryavanshi (RR) — 776 runs")

    st.divider()

    # Purple Cap
    st.subheader("🟣 Purple Cap — Final")
    pc = [{"#": i, "Player": p["name"], "Team": p["team"],
            "Wkts": p["wickets"], "Econ": p["econ"]}
           for i, p in enumerate(IPL_2026_LIVE["purple_cap"], 1)]
    st.dataframe(pd.DataFrame(pc), use_container_width=True,
                 hide_index=True, height=220)
    st.caption("🏅 Winner: Kagiso Rabada (GT) — 29 wickets")

    st.divider()

    # Playoff results
    st.subheader("🏆 Playoff Results")
    for r in IPL_2026_LIVE["recent_results"]:
        st.markdown(
            f'<div class="result-card">'
            f'<b>{r["match_no"]}:</b> {r["result"]}<br>'
            f'🏅 POTM: {r["potm"]}<br>'
            f'<span style="color:#666">🏟️ {r["venue"]} · {r["date"]}</span>'
            f'</div>', unsafe_allow_html=True)

    st.divider()
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_tokens = 0
        st.rerun()
    st.caption(f"🔢 Tokens: `{st.session_state.total_tokens:,}`")
    st.caption("Groq · llama-3.3-70b-versatile · Updated June 1, 2026")


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

    if prompt := st.chat_input("Ask about IPL 2026 final, awards, squads, history..."):
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
