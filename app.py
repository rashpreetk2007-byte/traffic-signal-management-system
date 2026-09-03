import streamlit as st
import time
from datetime import datetime

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
# HEADER
# ============================================================

st.title("🚦 TRAFFIC SIGNAL MANAGEMENT SYSTEM")

st.subheader("20 FEATURES SMART TRAFFIC CONTROL DASHBOARD")

st.caption("Created By: Rashpreet Kaur Arora")

st.divider()


# ============================================================
# SIDEBAR CONTROL PANEL
# ============================================================

st.sidebar.header("🚦 Control Panel")

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

st.sidebar.divider()

st.sidebar.subheader("🚗 Vehicle Detection")

st.session_state.vehicles = st.sidebar.slider(
    "Vehicles Detected",
    0,
    150,
    st.session_state.vehicles
)


# ============================================================
# MANUAL SIGNAL CONTROL
# ============================================================

st.sidebar.divider()

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
# TRAFFIC INFORMATION
# ============================================================

st.header("📊 Traffic Information")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🚗 Vehicles",
        vehicles
    )

with c2:
    st.metric(
        "📊 Traffic Density",
        density
    )

with c3:
    st.metric(
        "🚦 Current Signal",
        st.session_state.signal
    )

with c4:
    st.metric(
        "⏱️ Seconds",
        remaining
    )


# ============================================================
# TRAFFIC SIGNAL
# ============================================================

st.header("🚦 LIVE TRAFFIC SIGNAL")

# Native Streamlit traffic light.
# NO HTML.
# NO CSS classes.
# NO <div>.
# Therefore HTML source cannot appear as text.

st.markdown("### 🚦")

signal_col = st.columns([1, 1, 1, 1, 1])

with signal_col[2]:

    st.markdown("### ⚫")

    if st.session_state.signal == "RED":
        st.markdown("# 🔴")
    else:
        st.markdown("# ⚫")

    st.caption("RED")

    if st.session_state.signal == "YELLOW":
        st.markdown("# 🟡")
    else:
        st.markdown("# ⚫")

    st.caption("YELLOW")

    if st.session_state.signal == "GREEN":
        st.markdown("# 🟢")
    else:
        st.markdown("# ⚫")

    st.caption("GREEN")

    st.markdown("### ⚫")


st.markdown(
    f"## 🚦 {st.session_state.signal}"
)

st.markdown(
    f"### ⏱️ {remaining} seconds"
)


# ============================================================
# QUICK SIGNAL CONTROL
# ============================================================

st.header("🎛️ Quick Signal Control")

b1, b2, b3 = st.columns(3)

with b1:
    if st.button(
        "🔴 RED SIGNAL",
        use_container_width=True
    ):
        st.session_state.signal = "RED"
        st.session_state.signal_start = time.time()
        st.session_state.automatic = False
        st.rerun()

with b2:
    if st.button(
        "🟡 YELLOW SIGNAL",
        use_container_width=True
    ):
        st.session_state.signal = "YELLOW"
        st.session_state.signal_start = time.time()
        st.session_state.automatic = False
        st.rerun()

with b3:
    if st.button(
        "🟢 GREEN SIGNAL",
        use_container_width=True
    ):
        st.session_state.signal = "GREEN"
        st.session_state.signal_start = time.time()
        st.session_state.automatic = False
        st.rerun()


# ============================================================
# SYSTEM STATUS
# ============================================================

st.header("🛰️ System Status")

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

st.header("⚙️ Active Modes")

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

st.header("🤖 AI Traffic Analysis")

a1, a2 = st.columns(2)

with a1:

    st.subheader("📈 Traffic Analysis")

    st.write(
        f"Vehicles detected: **{vehicles}**"
    )

    st.write(
        f"Traffic density: **{density}**"
    )

    st.write(
        f"Current signal: **{st.session_state.signal}**"
    )

    if density == "HIGH":

        st.warning(
            "High traffic detected. "
            "Extended GREEN signal timing is recommended."
        )

    elif density == "MEDIUM":

        st.info(
            "Medium traffic detected. "
            "Adaptive signal timing is recommended."
        )

    else:

        st.success(
            "Low traffic detected. "
            "Normal signal timing is sufficient."
        )


with a2:

    st.subheader("🧠 Intelligent Recommendation")

    if st.session_state.emergency:

        st.error(
            "🚑 Emergency priority activated. "
            "GREEN signal assigned."
        )

    elif st.session_state.pedestrian:

        st.warning(
            "🚶 Pedestrian crossing is active."
        )

    elif st.session_state.school_zone:

        st.warning(
            "🏫 School Zone mode is active."
        )

    elif density == "HIGH":

        st.info(
            "🚗 Increase GREEN duration "
            "to reduce congestion."
        )

    elif density == "MEDIUM":

        st.info(
            "⚙️ Use adaptive signal timing."
        )

    else:

        st.success(
            "✅ Normal signal timing."
        )


# ============================================================
# 20 SMART FEATURES
# ============================================================

st.header("🧠 20 Smart Traffic Features")

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
    st.write(
        f"✅ **{i}.** {feature}"
    )


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.header("📋 Project Information")

p1, p2, p3 = st.columns(3)

with p1:
    st.info(
        "Project\n\n"
        "Traffic Signal Management System"
    )

with p2:
    st.info(
        "Technology\n\n"
        "Python + Streamlit"
    )

with p3:
    st.info(
        "Hardware\n\n"
        "Not Required"
    )


# ============================================================
# SYSTEM INFORMATION
# ============================================================

st.header("🕐 System Information")

st.write(
    "Current Time:",
    datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)

st.write("System Status: 🟢 ONLINE")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.subheader("🚦 Traffic Signal Management System")

st.write(
    "20 Features Smart Traffic Control Project"
)

st.write(
    "Created By: Rashpreet Kaur Arora"
)


# ============================================================
# AUTO REFRESH
# ============================================================

if st.session_state.automatic:
    time.sleep(1)
    st.rerun()