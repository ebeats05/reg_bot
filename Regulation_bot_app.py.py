import streamlit as st

# Strategy Cards with Māori Atua references
strategies = {
    "Red": {
        "Physical Aggression": {
            "ADHD": [
                "🔥 TE WHARE WAIORA CARD 🔥",
                "Atua: Tūmatauenga — Strength, War, and Conflict",
                "- Safe space with no demand",
                "- Use weighted tool",
                "- Soft background music"
            ],
            "Autism": [
                "🔥 KOIWI CARD 🔥",
                "Atua: Tūmatauenga — Strength, War, and Conflict",
                "- Remove overstimulation",
                "- Deep pressure item",
                "- Familiar adult support"
            ],
            "APD": [
                "🔥 KARAKIA CARD 🔥",
                "Atua: Tūmatauenga — Strength, War, and Conflict",
                "- Visual prompts only",
                "- Soft tone, no instructions",
                "- Non-verbal support"
            ],
            "None": [
                "🔥 RESET SPACE CARD 🔥",
                "Atua: Tūmatauenga — Strength, War, and Conflict",
                "- Space and silence",
                "- Breathing visuals",
                "- Quiet activity"
            ]
        }
    }
}

st.title("🧠 Regulation Support Bot")
st.subheader("🌀 Select Zone, Behavior, and Neurotype to get support strategies")

zone = st.selectbox("🌈 Choose a Zone:", ["Red"])
if zone:
    behavior = st.selectbox("🧠 Choose a Behavior:", list(strategies[zone].keys()))
    if behavior:
        profile = st.selectbox("🎯 Select Neurodiverse Profile:", ["ADHD", "Autism", "APD", "None"])
        if profile:
            st.markdown("### 📘 Strategy Card")
            for line in strategies[zone][behavior][profile]:
                st.markdown(f"- {line}")
streamlit, run, Regulation_bot_app.py



