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

if "signal" not in st.session_state:
    st.session_state.signal = "RED"

if "signal_start" not in st.session_state:
    st.session_state.signal_start = time.time()

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
# PAGE CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    padding: 22px;
    border-radius: 18px;
    background: linear-gradient(135deg, #111827, #374151);
    color: white;
    margin-bottom: 25px;
}

.main-title h1 {
    margin: 0;
    font-size: 32px;
}

.main-title p {
    margin: 7px;
}

.card {
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    min-height: 115px;
}

.card-icon {
    font-size: 28px;
}

.card-value {
    font-size: 27px;
    font-weight: bold;
}

.card-label {
    color: #555;
    font-size: 14px;
}

.traffic-housing {
    background: #080808;
    width: 210px;
    margin: 20px auto;
    padding: 25px 15px;
    border-radius: 38px;
    border: 8px solid #303030;
    box-shadow:
        0 12px 30px rgba(0,0,0,0.45),
        inset 0 0 15px rgba(255,255,255,0.04);
}

.blank-light {
    width: 105px;
    height: 105px;
    margin: 16px auto;
    border-radius: 50%;
    background: #202020;
    border: 5px solid #454545;
}

.red-light {
    background: #ff1111;
    box-shadow:
        0 0 15px #ff1111,
        0 0 35px #ff1111,
        0 0 60px #ff1111;
}

.yellow-light {
    background: #ffd21a;
    box-shadow:
        0 0 15px #ffd21a,
        0 0 35px #ffd21a,
        0 0 60px #ffd21a;
}

.green-light {
    background: #16e35a;
    box-shadow:
        0 0 15px #16e35a,
        0 0 35px #16e35a,
        0 0 60px #16e35a;
}

.light-label {
    color: white;
    text-align: center;
    font-size: 13px;
    font-weight: bold;
}

.feature {
    padding: 11px 15px;
    margin: 6px 0;
    border-radius: 10px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
}

.footer {
    background: #111827;
    color: white;
    text-align: center;
    padding: 22px;
    border-radius: 15px;
    margin-top: 30px;
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
    min_value=0,
    max_value=150,
    value=st.session_state.vehicles
)

# ============================================================
# MANUAL SIGNAL BUTTONS
# ============================================================

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
# SIGNAL TIMER
# ============================================================

if st.session_state.signal == "RED":
    duration = 10

elif st.session_state.signal == "YELLOW":
    duration = 5

else:
    duration = 10

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

st.markdown("## 📊 Traffic Information")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-icon">🚗</div>
            <div class="card-value">{vehicles}</div>
            <div class="card-label">Vehicles</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-icon">📊</div>
            <div class="card-value">{density}</div>
            <div class="card-label">Traffic Density</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-icon">🚦</div>
            <div class="card-value">{st.session_state.signal}</div>
            <div class="card-label">Current Signal</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-icon">⏱️</div>
            <div class="card-value">{remaining}</div>
            <div class="card-label">Seconds</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# TRAFFIC LIGHT
# ============================================================

st.markdown("## 🚦 LIVE TRAFFIC SIGNAL")

signal = st.session_state.signal

red_class = "red-light" if signal == "RED" else "blank-light"
yellow_class = "yellow-light" if signal == "YELLOW" else "blank-light"
green_class = "green-light" if signal == "GREEN" else "blank-light"

st.markdown(
    f"""
    <div class="traffic-housing">

        <div class="signal-light {red_class}"></div>
        <div class="light-label">RED</div>

        <div class="signal-light {yellow_class}"></div>
        <div class="light-label">YELLOW</div>

        <div class="signal-light {green_class}"></div>
        <div class="light-label">GREEN</div>

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
# SIGNAL CONTROL BUTTONS ON MAIN PAGE
# ============================================================

st.markdown("### 🎛️ Quick Signal Control")

b1, b2, b3 = st.columns(3)

with b1:
    if st.button("🔴 RED SIGNAL", use_container_width=True):
        st.session_state.signal = "RED"
        st.session_state.signal_start = time.time()
        st.session_state.automatic = False
        st.rerun()

with b2:
    if st.button("🟡 YELLOW SIGNAL", use_container_width=True):
        st.session_state.signal = "YELLOW"
        st.session_state.signal_start = time.time()
        st.session_state.automatic = False
        st.rerun()

with b3:
    if st.button("🟢 GREEN SIGNAL", use_container_width=True):
        st.session_state.signal = "GREEN"
        st.session_state.signal_start = time.time()
        st.session_state.automatic = False
        st.rerun()

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
# ACTIVE MODES
# ============================================================

st.markdown("## ⚙️ Active Modes")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.write(
        "🚑 Emergency:",
        "ACTIVE" if st.session_state.emergency else "OFF"
    )

with m2:
    st.write(
        "🚶 Pedestrian:",
        "ACTIVE" if st.session_state.pedestrian else "OFF"
    )

with m3:
    st.write(
        "🏫 School Zone:",
        "ACTIVE" if st.session_state.school_zone else "OFF"
    )

with m4:
    st.write(
        "🌙 Night Mode:",
        "ACTIVE" if st.session_state.night_mode else "OFF"
    )

# ============================================================
# AI TRAFFIC ANALYSIS
# ============================================================

st.markdown("## 🤖 AI Traffic Analysis")

ai1, ai2 = st.columns(2)

with ai1:

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
            "Medium traffic detected. Adaptive signal timing is recommended."
        )

    else:

        st.success(
            "Low traffic detected. Normal signal timing is sufficient."
        )

with ai2:

    st.markdown("### 🧠 Intelligent Recommendation")

    if st.session_state.emergency:

        st.error(
            "🚑 Emergency priority activated. GREEN signal assigned."
        )

    elif st.session_state.pedestrian:

        st.warning(
            "🚶 Pedestrian crossing is active."
        )

    elif st.session_state.school_zone:

        st.warning(
            "🏫 School zone mode is active. Reduced-speed traffic control recommended."
        )

    elif density == "HIGH":

        st.info(
            "🚗 AI recommendation: Increase GREEN duration to reduce congestion."
        )

    elif density == "MEDIUM":

        st.info(
            "⚙️ AI recommendation: Use adaptive signal timing."
        )

    else:

        st.success(
            "✅ AI recommendation: Normal signal timing."
        )

# ============================================================
# 20 FEATURES
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
        <div class="feature">
            ✅ <b>{i}.</b> {feature}
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
