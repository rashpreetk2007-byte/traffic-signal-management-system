import streamlit as st
import time
from datetime import datetime

# ============================================================
# TRAFFIC SIGNAL MANAGEMENT SYSTEM
# 20 FEATURES SMART TRAFFIC CONTROL DASHBOARD
# Created By: Rashpreet Kaur Arora
# Technology: Python + Streamlit
# Hardware: NOT REQUIRED
# ============================================================

st.set_page_config(
    page_title="Traffic Signal Management System",
    page_icon="🚦",
    layout="wide"
)

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "signal": "RED",
    "signal_start": time.time(),
    "vehicles": 45,
    "automatic": True,
    "emergency": False,
    "pedestrian": False,
    "school_zone": False,
    "night_mode": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    background: linear-gradient(135deg, #111827, #374151);
    color: white;
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 25px;
}

.main-title h1 {
    margin: 0;
    font-size: 32px;
}

.main-title p {
    margin: 7px 0;
}

.info-card {
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    min-height: 120px;
}

.info-icon {
    font-size: 28px;
}

.info-number {
    font-size: 28px;
    font-weight: bold;
}

.info-label {
    font-size: 14px;
    color: #555;
}

.signal-container {
    display: flex;
    justify-content: center;
    margin: 25px 0;
}

.signal-body {
    background: #101010;
    border: 7px solid #333333;
    border-radius: 32px;
    padding: 20px 22px 25px 22px;
    width: 190px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.35);
}

.signal-light {
    width: 105px;
    height: 105px;
    border-radius: 50%;
    margin: 12px auto;
    border: 5px solid #444;
    background: #252525;
}

.red-on {
    background: #ff0000;
    box-shadow:
        0 0 15px #ff0000,
        0 0 35px #ff0000,
        0 0 65px #ff0000;
}

.yellow-on {
    background: #ffd000;
    box-shadow:
        0 0 15px #ffd000,
        0 0 35px #ffd000,
        0 0 65px #ffd000;
}

.green-on {
    background: #00d94f;
    box-shadow:
        0 0 15px #00d94f,
        0 0 35px #00d94f,
        0 0 65px #00d94f;
}

.signal-name {
    color: white;
    text-align: center;
    font-weight: bold;
    font-size: 13px;
    margin-bottom: 10px;
}

.status-box {
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    border: 1px solid #ddd;
}

.feature {
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    padding: 11px 15px;
    margin: 7px 0;
    border-radius: 10px;
}

.footer {
    margin-top: 30px;
    background: #111827;
    color: white;
    text-align: center;
    padding: 22px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="main-title">
    <h1>🚦 TRAFFIC SIGNAL MANAGEMENT SYSTEM</h1>
    <p><b>20 FEATURES SMART TRAFFIC CONTROL DASHBOARD</b></p>
    <p>Created By: <b>Rashpreet Kaur Arora</b></p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🚦 Control Panel")

st.session_state.automatic = st.sidebar.toggle(
    "Automatic Signal",
    value=st.session_state.automatic
)

st.session_state.emergency = st.sidebar.toggle(
    "🚑 Emergency Mode",
    value=st.session_state.emergency
)

st.session_state.pedestrian = st.sidebar.toggle(
    "🚶 Pedestrian Crossing",
    value=st.session_state.pedestrian
)

st.session_state.school_zone = st.sidebar.toggle(
    "🏫 School Zone",
    value=st.session_state.school_zone
)

st.session_state.night_mode = st.sidebar.toggle(
    "🌙 Night Mode",
    value=st.session_state.night_mode
)

st.sidebar.markdown("---")

st.sidebar.subheader("🚗 Vehicle Detection")

st.session_state.vehicles = st.sidebar.slider(
    "Vehicles Detected",
    0,
    150,
    st.session_state.vehicles
)

st.sidebar.markdown("---")

st.sidebar.subheader("🎛️ Manual Signal Control")

if st.sidebar.button("🔴 RED", use_container_width=True):
    st.session_state.signal = "RED"
    st.session_state.signal_start = time.time()
    st.session_state.automatic = False
    st.rerun()

if st.sidebar.button("🟡 YELLOW", use_container_width=True):
    st.session_state.signal = "YELLOW"
    st.session_state.signal_start = time.time()
    st.session_state.automatic = False
    st.rerun()

if st.sidebar.button("🟢 GREEN", use_container_width=True):
    st.session_state.signal = "GREEN"
    st.session_state.signal_start = time.time()
    st.session_state.automatic = False
    st.rerun()

# ============================================================
# TRAFFIC DENSITY
# ============================================================

vehicles = st.session_state.vehicles

if vehicles <= 30:
    density = "LOW"
elif vehicles <= 80:
    density = "MEDIUM"
else:
    density = "HIGH"

# ============================================================
# SIGNAL TIMING
# ============================================================

if st.session_state.signal == "RED":
    duration = 10
elif st.session_state.signal == "YELLOW":
    duration = 5
else:
    duration = 10

# Emergency mode
if st.session_state.emergency:
    st.session_state.signal = "GREEN"
    duration = 15

elapsed = int(time.time() - st.session_state.signal_start)
remaining = max(0, duration - elapsed)

# ============================================================
# AUTOMATIC SIGNAL
# ============================================================

if st.session_state.automatic and not st.session_state.emergency:

    if elapsed >= duration:

        if st.session_state.signal == "RED":
            st.session_state.signal = "GREEN"

        elif st.session_state.signal == "GREEN":
            st.session_state.signal = "YELLOW"

        else:
            st.session_state.signal = "RED"

        st.session_state.signal_start = time.time()
        st.rerun()

# ============================================================
# INFORMATION CARDS
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-icon">🚗</div>
            <div class="info-number">{vehicles}</div>
            <div class="info-label">Vehicles</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-icon">📊</div>
            <div class="info-number">{density}</div>
            <div class="info-label">Traffic Density</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-icon">🚦</div>
            <div class="info-number">{st.session_state.signal}</div>
            <div class="info-label">Current Signal</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-icon">⏱️</div>
            <div class="info-number">{remaining}</div>
            <div class="info-label">Seconds</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# LIVE TRAFFIC SIGNAL
# ============================================================

st.markdown("## 🚦 LIVE TRAFFIC SIGNAL")

signal = st.session_state.signal

red_class = "red-on" if signal == "RED" else ""
yellow_class = "yellow-on" if signal == "YELLOW" else ""
green_class = "green-on" if signal == "GREEN" else ""

st.markdown(
    f"""
    <div class="signal-container">
        <div class="signal-body">

            <div class="signal-light {red_class}"></div>
            <div class="signal-name">RED</div>

            <div class="signal-light {yellow_class}"></div>
            <div class="signal-name">YELLOW</div>

            <div class="signal-light {green_class}"></div>
            <div class="signal-name">GREEN</div>

        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align:center;">
        <h2>🚦 {signal}</h2>
        <h3>⏱️ {remaining} seconds</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SYSTEM STATUS
# ============================================================

st.markdown("## 🛰️ System Status")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.success("SYSTEM RUNNING")

with s2:
    if st.session_state.automatic:
        st.info("AUTOMATIC MODE")
    else:
        st.warning("MANUAL MODE")

with s3:
    if density == "HIGH":
        st.error("HIGH TRAFFIC")
    elif density == "MEDIUM":
        st.warning("MEDIUM TRAFFIC")
    else:
        st.success("LOW TRAFFIC")

with s4:
    if st.session_state.pedestrian:
        st.warning("PEDESTRIAN CROSSING")
    else:
        st.success("ROAD CLEAR")

# ============================================================
# SPECIAL MODES
# ============================================================

st.markdown("## ⚙️ Active Modes")

m1, m2, m3, m4 = st.columns(4)

with m1:
    if st.session_state.emergency:
        st.error("🚑 EMERGENCY ACTIVE")
    else:
        st.success("NORMAL EMERGENCY MODE")

with m2:
    if st.session_state.pedestrian:
        st.warning("🚶 CROSSING ACTIVE")
    else:
        st.success("PEDESTRIAN NORMAL")

with m3:
    if st.session_state.school_zone:
        st.warning("🏫 SCHOOL ZONE ACTIVE")
    else:
        st.success("NORMAL ZONE")

with m4:
    if st.session_state.night_mode:
        st.info("🌙 NIGHT MODE ACTIVE")
    else:
        st.success("☀️ DAY MODE")

# ============================================================
# SMART TRAFFIC ANALYSIS
# ============================================================

st.markdown("## 🤖 Smart Traffic Analysis")

a1, a2 = st.columns(2)

with a1:
    st.markdown("### 📈 Traffic Analysis")

    st.write(f"**Vehicles detected:** {vehicles}")
    st.write(f"**Traffic density:** {density}")
    st.write(f"**Current signal:** {signal}")

    if density == "HIGH":
        st.error(
            "High traffic detected. Extended GREEN signal timing is recommended."
        )

    elif density == "MEDIUM":
        st.warning(
            "Medium traffic detected. Adaptive timing is recommended."
        )

    else:
        st.success(
            "Low traffic detected. Normal signal timing is sufficient."
        )

with a2:
    st.markdown("### 🧠 Intelligent Recommendation")

    if st.session_state.emergency:
        st.error(
            "🚑 Emergency priority activated. GREEN signal assigned."
        )

    elif st.session_state.pedestrian:
        st.warning(
            "🚶 Pedestrian crossing is currently active."
        )

    elif st.session_state.school_zone:
        st.warning(
            "🏫 School zone mode is active. Drive carefully."
        )

    elif density == "HIGH":
        st.info(
            "🚗 Increase GREEN duration to reduce congestion."
        )

    elif density == "MEDIUM":
        st.info(
            "⚙️ Use adaptive signal timing."
        )

    else:
        st.success(
            "✅ Traffic conditions are normal."
        )

# ============================================================
# TRAFFIC STATISTICS
# ============================================================

st.markdown("## 📊 Traffic Statistics")

stat1, stat2, stat3 = st.columns(3)

with stat1:
    st.metric(
        "Vehicles Detected",
        vehicles
    )

with stat2:
    if density == "HIGH":
        recommendation = "Extended"
    elif density == "MEDIUM":
        recommendation = "Adaptive"
    else:
        recommendation = "Normal"

    st.metric(
        "Signal Timing",
        recommendation
    )

with stat3:
    st.metric(
        "Current Signal",
        signal
    )

# ============================================================
# 20 SMART FEATURES
# ============================================================

st.markdown("## 🧠 20 Smart Traffic Features")

features = [
    "Automatic Traffic Signal Control",
    "Real-Time Signal Status",
    "Traffic Density Detection",
    "Vehicle Count Monitoring",
    "Adaptive Signal Timing",
    "Emergency Vehicle Priority",
    "Pedestrian Crossing Management",
    "Accident Alert System",
    "Traffic Congestion Detection",
    "Wrong-Way Vehicle Alert",
    "Ambulance Priority",
    "Fire Brigade Priority",
    "School Zone Traffic Mode",
    "Night Traffic Mode",
    "Manual Signal Override",
    "Traffic Statistics",
    "Signal Countdown Timer",
    "Smart Route Recommendation",
    "Traffic Incident Monitoring",
    "Traffic Management Dashboard"
]

for number, feature in enumerate(features, 1):
    st.markdown(
        f"""
        <div class="feature">
            ✅ <b>{number}.</b> {feature}
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# PROJECT INFORMATION
# ============================================================

st.markdown("## 📋 Project Information")

p1, p2, p3 = st.columns(3)

with p1:
    st.info(
        "**Project**\n\n"
        "Traffic Signal Management System"
    )

with p2:
    st.info(
        "**Technology**\n\n"
        "Python + Streamlit"
    )

with p3:
    st.info(
        "**Hardware**\n\n"
        "Not Required"
    )

# ============================================================
# SYSTEM INFORMATION
# ============================================================

st.markdown("## 🕐 System Information")

st.write(
    "Current Time:",
    datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)

st.write("System Status: 🟢 ONLINE")

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        <h3>🚦 Traffic Signal Management System</h3>
        <p>20 Features Smart Traffic Control Project</p>
        <p>Created By: <b>Rashpreet Kaur Arora</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# AUTO REFRESH
# ============================================================

if st.session_state.automatic:
    time.sleep(1)
    st.rerun()
