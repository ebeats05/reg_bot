
import streamlit as st

# Strategy dictionary
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
        },
        "Verbal Outbursts": {
            "ADHD": [
                "🔥 TIME-IN CARD 🔥",
                "Atua: Tūmatauenga — Strength, War, and Conflict",
                "- Reflective drawing",
                "- Fidget + breathing",
                "- Calm voice"
            ],
            "Autism": [
                "🔥 WHAKATA CARD 🔥",
                "Atua: Tūmatauenga — Strength, War, and Conflict",
                "- Avoid eye contact",
                "- Comic strip support",
                "- Visual sequence"
            ],
            "APD": [
                "🔥 TŪRANGAWAEWAE CARD 🔥",
                "Atua: Tūmatauenga — Strength, War, and Conflict",
                "- Gesture to activity",
                "- No verbal demands",
                "- Sit nearby silently"
            ],
            "None": [
                "🔥 DEESCALATION CARD 🔥",
                "Atua: Tūmatauenga — Strength, War, and Conflict",
                "- Whisper voice",
                "- Breathing image",
                "- Calm tone"
            ]
        }
    }
}

# Streamlit App UI
st.set_page_config(page_title="Regulation Support Bot", layout="centered")
st.title("🧠 Regulation Support Bot")
st.caption("Guided by Te Ao Māori and the Zones of Regulation")

zone = st.selectbox("🌈 Choose a Zone of Regulation:", list(strategies.keys()))
if zone:
    behavior = st.selectbox("🧠 What behaviour are you noticing?", list(strategies[zone].keys()))
    if behavior:
        profile = st.selectbox("🎯 Select Neurodiverse Profile:", list(strategies[zone][behavior].keys()))
        if profile:
            st.markdown("### 📘 Strategy Card")
            for line in strategies[zone][behavior][profile]:
                st.markdown(f"- {line}")
