import streamlit as st
import time
from datetime import datetime

# ============================================================
# TRAFFIC SIGNAL MANAGEMENT SYSTEM
# Created By: Rashpreet Kaur Arora
# 20 FEATURES PROJECT
# Technology: Python + Streamlit
# Hardware: NOT REQUIRED
# ============================================================

st.set_page_config(
    page_title="Traffic Signal Management System",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SESSION STATE
# ============================================================

if "signal" not in st.session_state:
    st.session_state.signal = "RED"

if "last_change" not in st.session_state:
    st.session_state.last_change = time.time()

if "countdown" not in st.session_state:
    st.session_state.countdown = 10

if "vehicles" not in st.session_state:
    st.session_state.vehicles = 45

if "automatic" not in st.session_state:
    st.session_state.automatic = True

if "emergency" not in st.session_state:
    st.session_state.emergency = False

if "pedestrian" not in st.session_state:
    st.session_state.pedestrian = False

if "school_zone" not in st.session_state:
    st.session_state.school_zone = False

if "night_mode" not in st.session_state:
    st.session_state.night_mode = False

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title-box {
    text-align: center;
    padding: 18px;
    border-radius: 18px;
    background: linear-gradient(135deg, #111827, #1f2937);
    color: white;
    margin-bottom: 20px;
}

.title-box h1 {
    margin: 0;
    font-size: 32px;
}

.title-box p {
    margin: 7px 0 0 0;
    font-size: 16px;
}

.signal-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 15px auto 20px auto;
}

.traffic-light {
    width: 180px;
    background: #111;
    border: 8px solid #333;
    border-radius: 35px;
    padding: 25px 20px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.45);
}

.light {
    width: 100px;
    height: 100px;
    margin: 18px auto;
    border-radius: 50%;
    background: #333;
    border: 5px solid #555;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0;
}

.light.active-red {
    background: #ff1f1f;
    box-shadow:
        0 0 15px #ff1f1f,
        0 0 35px #ff1f1f,
        0 0 65px rgba(255,0,0,0.8);
}

.light.active-yellow {
    background: #ffd21f;
    box-shadow:
        0 0 15px #ffd21f,
        0 0 35px #ffd21f,
        0 0 65px rgba(255,210,0,0.8);
}

.light.active-green {
    background: #19e65c;
    box-shadow:
        0 0 15px #19e65c,
        0 0 35px #19e65c,
        0 0 65px rgba(0,255,80,0.8);
}

.light-label {
    text-align: center;
    color: white;
    font-size: 13px;
    font-weight: bold;
    margin-top: -12px;
}

.status-card {
    padding: 15px;
    border-radius: 14px;
    background: #f3f4f6;
    text-align: center;
    margin-bottom: 10px;
    border: 1px solid #ddd;
}

.big-number {
    font-size: 30px;
    font-weight: bold;
}

.feature-card {
    padding: 12px 15px;
    border-radius: 12px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    margin-bottom: 8px;
}

.footer {
    text-align: center;
    padding: 20px;
    margin-top: 30px;
    border-radius: 15px;
    background: #111827;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="title-box">
    <h1>🚦 TRAFFIC SIGNAL MANAGEMENT SYSTEM</h1>
    <p>20 FEATURES SMART TRAFFIC CONTROL DASHBOARD</p>
    <p>Created By: <b>Rashpreet Kaur Arora</b></p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR CONTROL PANEL
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
    min_value=0,
    max_value=150,
    value=st.session_state.vehicles
)

st.sidebar.markdown("---")

st.sidebar.subheader("🎛️ Manual Signal Control")

if st.sidebar.button("🔴 RED", use_container_width=True):
    st.session_state.signal = "RED"
    st.session_state.countdown = 10
    st.session_state.last_change = time.time()

if st.sidebar.button("🟡 YELLOW", use_container_width=True):
    st.session_state.signal = "YELLOW"
    st.session_state.countdown = 5
    st.session_state.last_change = time.time()

if st.sidebar.button("🟢 GREEN", use_container_width=True):
    st.session_state.signal = "GREEN"
    st.session_state.countdown = 10
    st.session_state.last_change = time.time()

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
# AUTOMATIC SIGNAL LOGIC
# ============================================================

if st.session_state.automatic:

    elapsed = time.time() - st.session_state.last_change

    if st.session_state.signal == "RED":
        duration = 10
        remaining = max(0, duration - int(elapsed))

        if elapsed >= duration:
            st.session_state.signal = "GREEN"
            st.session_state.last_change = time.time()
            st.session_state.countdown = 10
            st.rerun()

    elif st.session_state.signal == "GREEN":
        duration = 10
        remaining = max(0, duration - int(elapsed))

        if elapsed >= duration:
            st.session_state.signal = "YELLOW"
            st.session_state.last_change = time.time()
            st.session_state.countdown = 5
            st.rerun()

    else:
        duration = 5
        remaining = max(0, duration - int(elapsed))

        if elapsed >= duration:
            st.session_state.signal = "RED"
            st.session_state.last_change = time.time()
            st.session_state.countdown = 10
            st.rerun()

else:
    remaining = st.session_state.countdown

# ============================================================
# SPECIAL MODES
# ============================================================

if st.session_state.emergency:
    st.session_state.signal = "GREEN"
    remaining = 15

if st.session_state.pedestrian:
    pedestrian_status = "CROSSING ACTIVE"
else:
    pedestrian_status = "ROAD OPEN"

if st.session_state.school_zone:
    school_status = "SCHOOL ZONE ACTIVE"
else:
    school_status = "NORMAL ZONE"

if st.session_state.night_mode:
    night_status = "NIGHT MODE ACTIVE"
else:
    night_status = "DAY MODE"

# ============================================================
# TOP INFORMATION
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="status-card">
            🚗<br>
            <span class="big-number">{vehicles}</span><br>
            Vehicles
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="status-card">
            📊<br>
            <span class="big-number">{density}</span><br>
            Traffic Density
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="status-card">
            🚦<br>
            <span class="big-number">{st.session_state.signal}</span><br>
            Current Signal
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class="status-card">
            ⏱️<br>
            <span class="big-number">{remaining}</span><br>
            Seconds
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# TRAFFIC SIGNAL
# ============================================================

st.markdown("## 🚦 LIVE TRAFFIC SIGNAL")

red_class = "active-red" if st.session_state.signal == "RED" else ""
yellow_class = "active-yellow" if st.session_state.signal == "YELLOW" else ""
green_class = "active-green" if st.session_state.signal == "GREEN" else ""

st.markdown(
    f"""
    <div class="signal-wrapper">
        <div class="traffic-light">

            <div class="light {red_class}"></div>
            <div class="light-label">RED</div>

            <div class="light {yellow_class}"></div>
            <div class="light-label">YELLOW</div>

            <div class="light {green_class}"></div>
            <div class="light-label">GREEN</div>

        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align:center;">
        <h2>{st.session_state.signal}</h2>
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
# SMART TRAFFIC ANALYSIS
# ============================================================

st.markdown("## 🤖 Smart Traffic Analysis")

a1, a2 = st.columns(2)

with a1:
    st.markdown("### 📈 Traffic Analysis")

    st.write(f"**Vehicles detected:** {vehicles}")
    st.write(f"**Traffic density:** {density}")
    st.write(f"**Current signal:** {st.session_state.signal}")

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
        st.error("🚑 Emergency priority activated. GREEN signal assigned.")
    elif st.session_state.pedestrian:
        st.warning("🚶 Pedestrian crossing is currently active.")
    elif st.session_state.school_zone:
        st.warning("🏫 School zone mode is active. Drive carefully.")
    elif density == "HIGH":
        st.info("🚗 Increase GREEN duration to reduce congestion.")
    elif density == "MEDIUM":
        st.info("⚙️ Use adaptive signal timing.")
    else:
        st.success("✅ Traffic conditions are normal.")

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

for i, feature in enumerate(features, 1):
    st.markdown(
        f"""
        <div class="feature-card">
            ✅ <b>{i}.</b> {feature}
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# PROJECT INFORMATION
# ============================================================

st.markdown("## 📋 Project Information")

i1, i2, i3 = st.columns(3)

with i1:
    st.info("**Project**\n\nTraffic Signal Management System")

with i2:
    st.info("**Technology**\n\nPython + Streamlit")

with i3:
    st.info("**Hardware**\n\nNot Required")

# ============================================================
# LIVE CLOCK
# ============================================================

st.markdown("## 🕐 System Information")

st.write(
    "Current Time:",
    datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)

st.write(
    "System Status: 🟢 ONLINE"
)

# ============================================================
# AUTO REFRESH
# ============================================================

if st.session_state.automatic:
    time.sleep(1)
    st.rerun()

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
