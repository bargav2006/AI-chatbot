"""
IPL Cricket Expert Chatbot — Streamlit App
Powered by Groq API (llama-3.3-70b-versatile)
Live IPL 2026 data: points table, Orange/Purple Cap, upcoming matches, stats
"""

import streamlit as st
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
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&family=DM+Sans:wght@400;500&display=swap');

.ipl-header {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 18px 24px; border-radius: 12px; margin-bottom: 16px;
    display: flex; align-items: center; gap: 16px;
    border: 1px solid rgba(247,201,72,0.3);
}
.ipl-header h1 { font-family: 'Rajdhani',sans-serif; color:#f7c948; font-size:24px; font-weight:700; margin:0; }
.ipl-header p  { color:rgba(255,255,255,0.6); font-size:12px; margin:0; }

.live-badge {
    display:inline-block; background:#e53935; color:#fff;
    font-size:10px; font-weight:700; padding:2px 7px; border-radius:10px;
    letter-spacing:1px; margin-left:6px; vertical-align:middle;
}
.stat-card {
    background:#1a1a2e; color:#f7c948; padding:12px 16px;
    border-radius:10px; text-align:center; border:1px solid rgba(247,201,72,0.2);
    margin-bottom:8px;
}
.stat-card .value { font-family:'Rajdhani',sans-serif; font-size:20px; font-weight:700; }
.stat-card .label { font-size:10px; color:rgba(255,255,255,0.5); margin-top:1px; }

.team-card {
    padding:7px 12px; border-radius:8px; margin-bottom:5px;
    font-size:12px; font-weight:500; border:1px solid rgba(0,0,0,0.08);
}
.match-card {
    background:#f8f9fa; border-radius:8px; padding:10px 14px;
    margin-bottom:8px; border-left:3px solid #f7c948; font-size:13px;
}
.points-row {
    display:flex; justify-content:space-between; align-items:center;
    padding:6px 0; border-bottom:1px solid #f0f0f0; font-size:12px;
}
.qualified { color:#16a34a; font-weight:700; }
.eliminated { color:#dc2626; font-weight:700; }
</style>
""", unsafe_allow_html=True)


# ── Groq client ────────────────────────────────────────────────────────────────
@st.cache_resource
def get_client() -> Groq:
    api_key = st.secrets.get("GROQ_API_KEY", None)
    if not api_key:
        st.error("⚠️ **Groq API key not found.** Add `GROQ_API_KEY = 'gsk_...'` to `.streamlit/secrets.toml`\nGet a free key at https://console.groq.com/keys")
        st.stop()
    return Groq(api_key=api_key)


# ── Session state ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0


# ── Layout: header + two columns ──────────────────────────────────────────────
st.markdown("""
<div class="ipl-header">
  <div style="font-size:34px">🏏</div>
  <div>
    <h1>IPL Cricket Expert <span class="live-badge">LIVE 2026</span></h1>
    <p>Season 19 · Updated through Match 64 · Ask about teams, players, records, live standings</p>
  </div>
</div>
""", unsafe_allow_html=True)

main_col, side_col = st.columns([2, 1])

# ══════════════════════════════════════════════════════════════════════════════
# RIGHT PANEL — live stats dashboard
# ══════════════════════════════════════════════════════════════════════════════
with side_col:
    pt = IPL_2026_LIVE["points_table"]

    # Points table
    st.markdown("#### 🏆 IPL 2026 Points Table")
    st.caption("After Match 64 · May 20, 2026")
    header_cols = st.columns([3,1,1,1,1])
    for h, c in zip(["Team","M","W","Pts","NRR"], header_cols):
        c.markdown(f"**{h}**")
    for row in pt:
        cols = st.columns([3,1,1,1,1])
        status = row.get("status","")
        color = "#16a34a" if status=="Q" else ("#dc2626" if status=="E" else "#1a1a2e")
        badge = " ✅" if status=="Q" else (" ❌" if status=="E" else "")
        cols[0].markdown(f'<span style="color:{color};font-size:12px;font-weight:600">{row["team"]}{badge}</span>', unsafe_allow_html=True)
        cols[1].markdown(f'<span style="font-size:12px">{row["m"]}</span>', unsafe_allow_html=True)
        cols[2].markdown(f'<span style="font-size:12px">{row["w"]}</span>', unsafe_allow_html=True)
        cols[3].markdown(f'<span style="font-size:12px;font-weight:700">{row["pts"]}</span>', unsafe_allow_html=True)
        cols[4].markdown(f'<span style="font-size:11px">{row["nrr"]}</span>', unsafe_allow_html=True)
    st.caption("✅ Qualified  ❌ Eliminated")

    st.divider()

    # Orange cap
    st.markdown("#### 🟠 Orange Cap — Top Scorers")
    for i, p in enumerate(IPL_2026_LIVE["orange_cap"], 1):
        st.markdown(f'<div style="font-size:12px;padding:3px 0;border-bottom:1px solid #f0f0f0">'
                    f'<b>{i}. {p["name"]}</b> <span style="color:#888">({p["team"]})</span>'
                    f' — <b style="color:#e8870a">{p["runs"]}</b> runs | SR {p["sr"]}'
                    f'</div>', unsafe_allow_html=True)

    st.divider()

    # Purple cap
    st.markdown("#### 🟣 Purple Cap — Top Wicket Takers")
    for i, p in enumerate(IPL_2026_LIVE["purple_cap"], 1):
        st.markdown(f'<div style="font-size:12px;padding:3px 0;border-bottom:1px solid #f0f0f0">'
                    f'<b>{i}. {p["name"]}</b> <span style="color:#888">({p["team"]})</span>'
                    f' — <b style="color:#7c3aed">{p["wickets"]}</b> wkts | Econ {p["econ"]}'
                    f'</div>', unsafe_allow_html=True)

    st.divider()

    # Upcoming matches
    st.markdown("#### 📅 Upcoming Matches")
    for m in IPL_2026_LIVE["upcoming_matches"]:
        st.markdown(
            f'<div class="match-card">'
            f'<div style="font-weight:700;font-size:13px">{m["team1"]} vs {m["team2"]}</div>'
            f'<div style="color:#666;font-size:11px">📅 {m["date"]} · {m["time"]} IST</div>'
            f'<div style="color:#666;font-size:11px">🏟️ {m["venue"]}</div>'
            f'<div style="color:#aaa;font-size:10px">Match {m["match_no"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.divider()

    # Season records
    st.markdown("#### 📊 IPL 2026 Season Stats")
    for label, val in IPL_2026_LIVE["season_stats"].items():
        st.markdown(
            f'<div class="match-card" style="border-left-color:#1a1a2e">'
            f'<span style="font-size:11px;color:#666">{label}</span><br>'
            f'<span style="font-size:13px;font-weight:700">{val}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.divider()
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_tokens = 0
        st.rerun()
    st.caption(f"🔢 Tokens: `{st.session_state.total_tokens:,}`")
    st.caption("Groq · llama-3.3-70b-versatile")


# ══════════════════════════════════════════════════════════════════════════════
# LEFT PANEL — chatbot
# ══════════════════════════════════════════════════════════════════════════════
with main_col:
    if not st.session_state.messages:
        st.markdown("#### 💡 Quick questions:")
        cols = st.columns(2)
        for i, q in enumerate(QUICK_QUESTIONS):
            if cols[i % 2].button(q, key=f"chip_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": q})
                st.rerun()

    for msg in st.session_state.messages:
        avatar = "🏏" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask about IPL 2026 standings, players, stats, history..."):
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