import streamlit as st
import time
import random

st.set_page_config(
    page_title="Traffic Signal Management System",
    page_icon="🚦",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "running" not in st.session_state:
    st.session_state.running = True

if "signal" not in st.session_state:
    st.session_state.signal = "RED"

if "last_change" not in st.session_state:
    st.session_state.last_change = time.time()

if "vehicle_count" not in st.session_state:
    st.session_state.vehicle_count = 42


# -----------------------------
# SIGNAL SETTINGS
# -----------------------------
DURATIONS = {
    "RED": 10,
    "GREEN": 10,
    "YELLOW": 4
}

NEXT_SIGNAL = {
    "RED": "GREEN",
    "GREEN": "YELLOW",
    "YELLOW": "RED"
}


def change_signal():
    st.session_state.signal = NEXT_SIGNAL[st.session_state.signal]
    st.session_state.last_change = time.time()


def light(active, emoji, name):
    if active:
        return f"""
        <div class="light active">
            <div class="circle">{emoji}</div>
            <div class="light-name">{name}</div>
        </div>
        """
    else:
        return f"""
        <div class="light">
            <div class="circle off">●</div>
            <div class="light-name">{name}</div>
        </div>
        """


# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.main-title {
    text-align:center;
    font-size:36px;
    font-weight:800;
    margin-bottom:5px;
}

.subtitle {
    text-align:center;
    font-size:18px;
    margin-bottom:25px;
}

.signal-box {
    width:180px;
    margin:auto;
    padding:22px;
    border-radius:30px;
    background:#181818;
    box-shadow:0 0 30px rgba(0,0,0,.35);
}

.light {
    text-align:center;
    margin:12px 0;
    opacity:.25;
}

.light.active {
    opacity:1;
}

.circle {
    width:75px;
    height:75px;
    border-radius:50%;
    margin:auto;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:48px;
}

.active .circle {
    animation: glow 1s infinite alternate;
}

.off {
    font-size:60px;
}

.light-name {
    color:white;
    font-weight:bold;
    margin-top:5px;
}

@keyframes glow {
    from {
        transform:scale(1);
        box-shadow:0 0 10px rgba(255,255,255,.3);
    }
    to {
        transform:scale(1.08);
        box-shadow:0 0 35px rgba(255,255,255,.9);
    }
}

.card {
    padding:20px;
    border-radius:15px;
    background:#f5f5f5;
    text-align:center;
    margin-bottom:10px;
}

.feature {
    padding:12px;
    border-radius:10px;
    background:#f7f7f7;
    margin-bottom:8px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<div class="main-title">🚦 TRAFFIC SIGNAL MANAGEMENT SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">20 FEATURES PROJECT | Smart Traffic Control Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    "<center><b>Created By: Rashpreet Kaur Arora</b></center>",
    unsafe_allow_html=True
)

st.divider()


# -----------------------------
# AUTOMATIC SIGNAL
# -----------------------------
if st.session_state.running:

    elapsed = int(time.time() - st.session_state.last_change)
    duration = DURATIONS[st.session_state.signal]
    remaining = duration - elapsed

    if remaining <= 0:
        change_signal()
        st.rerun()

else:
    remaining = DURATIONS[st.session_state.signal]


# -----------------------------
# MAIN DISPLAY
# -----------------------------
left, center, right = st.columns([1, 1, 1])

with left:

    st.subheader("📊 Traffic Status")

    st.metric(
        "Current Signal",
        st.session_state.signal
    )

    st.metric(
        "Vehicles Detected",
        st.session_state.vehicle_count
    )

    density = (
        "LOW"
        if st.session_state.vehicle_count < 30
        else "MEDIUM"
        if st.session_state.vehicle_count < 70
        else "HIGH"
    )

    st.metric(
        "Traffic Density",
        density
    )


with center:

    st.subheader("🚦 Live Traffic Signal")

    signal_html = f"""
    <div class="signal-box">

        {light(
            st.session_state.signal == "RED",
            "🔴",
            "RED"
        )}

        {light(
            st.session_state.signal == "YELLOW",
            "🟡",
            "YELLOW"
        )}

        {light(
            st.session_state.signal == "GREEN",
            "🟢",
            "GREEN"
        )}

    </div>
    """

    st.markdown(signal_html, unsafe_allow_html=True)

    st.markdown(
        f"<h2 style='text-align:center;'>⏱️ {remaining} seconds</h2>",
        unsafe_allow_html=True
    )


with right:

    st.subheader("⚙️ Signal Control")

    if st.button("🔄 Change Signal", use_container_width=True):
        change_signal()
        st.rerun()

    if st.session_state.running:

        if st.button("⏸️ Pause", use_container_width=True):
            st.session_state.running = False
            st.rerun()

    else:

        if st.button("▶️ Start Automatic Mode", use_container_width=True):
            st.session_state.running = True
            st.session_state.last_change = time.time()
            st.rerun()

    if st.button("🚗 Simulate Traffic", use_container_width=True):
        st.session_state.vehicle_count = random.randint(10, 120)
        st.rerun()


st.divider()


# -----------------------------
# 20 FEATURES
# -----------------------------
st.header("🧠 Smart Traffic Features")

features = [
    "1. Automatic Traffic Signal Control",
    "2. Real-Time Signal Status",
    "3. Traffic Density Detection",
    "4. Vehicle Count Monitoring",
    "5. Adaptive Signal Timing",
    "6. Emergency Vehicle Priority",
    "7. Pedestrian Crossing Management",
    "8. Accident Alert System",
    "9. Traffic Congestion Detection",
    "10. Wrong-Way Vehicle Alert",
    "11. Ambulance Priority",
    "12. Fire Brigade Priority",
    "13. School Zone Traffic Mode",
    "14. Night Traffic Mode",
    "15. Manual Signal Override",
    "16. Traffic Statistics",
    "17. Signal Countdown Timer",
    "18. Smart Route Recommendation",
    "19. Traffic Incident Monitoring",
    "20. Traffic Management Dashboard"
]

col1, col2 = st.columns(2)

for i, feature in enumerate(features):

    if i < 10:
        with col1:
            st.markdown(
                f'<div class="feature">✅ {feature}</div>',
                unsafe_allow_html=True
            )
    else:
        with col2:
            st.markdown(
                f'<div class="feature">✅ {feature}</div>',
                unsafe_allow_html=True
            )


# -----------------------------
# FOOTER
# -----------------------------
st.divider()

st.markdown(
    "<center>🚦 Smart Traffic Signal Management System<br>"
    "<b>Created By: Rashpreet Kaur Arora</b></center>",
    unsafe_allow_html=True
)

# Automatic refresh
if st.session_state.running:
    time.sleep(1)
    st.rerun()
