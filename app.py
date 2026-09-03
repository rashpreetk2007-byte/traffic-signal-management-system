import streamlit as st
import time
import random

# ============================================================
# TRAFFIC SIGNAL MANAGEMENT SYSTEM
# Created By: Rashpreet Kaur Arora
# 20 FEATURES PROJECT
# Hardware: NOT REQUIRED
# Streamlit Version
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

defaults = {
    "signal": "RED",
    "running": True,
    "last_change": time.time(),
    "vehicle_count": 45,
    "emergency": False,
    "pedestrian": False,
    "night_mode": False,
    "manual_mode": False,
    "accident": False,
    "wrong_way": False,
    "school_zone": False,
    "congestion": False,
    "green_time": 10,
    "yellow_time": 4,
    "red_time": 10
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# FUNCTIONS
# ============================================================

def get_duration():

    if st.session_state.signal == "GREEN":
        return st.session_state.green_time

    if st.session_state.signal == "YELLOW":
        return st.session_state.yellow_time

    return st.session_state.red_time


def next_signal():

    if st.session_state.signal == "RED":
        st.session_state.signal = "GREEN"

    elif st.session_state.signal == "GREEN":
        st.session_state.signal = "YELLOW"

    else:
        st.session_state.signal = "RED"

    st.session_state.last_change = time.time()


def calculate_density():

    count = st.session_state.vehicle_count

    if count < 30:
        return "LOW"

    elif count < 70:
        return "MEDIUM"

    return "HIGH"


def adaptive_timing():

    count = st.session_state.vehicle_count

    if count >= 90:
        st.session_state.green_time = 20

    elif count >= 70:
        st.session_state.green_time = 16

    elif count >= 40:
        st.session_state.green_time = 12

    else:
        st.session_state.green_time = 8


def signal_color():

    if st.session_state.signal == "RED":
        return "RED"

    if st.session_state.signal == "YELLOW":
        return "YELLOW"

    return "GREEN"


# ============================================================
# PAGE CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #eef2f7;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    margin-top: 10px;
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 5px;
}

.creator {
    text-align: center;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 20px;
}

.dashboard-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.status-card {
    text-align: center;
    background: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

.traffic-body {
    width: 190px;
    padding: 20px 20px 25px 20px;
    margin: 15px auto;
    border-radius: 35px;
    background: linear-gradient(
        145deg,
        #080808,
        #252525,
        #101010
    );

    border: 6px solid #444;

    box-shadow:
        0 15px 40px rgba(0,0,0,0.55),
        inset 0 0 25px rgba(255,255,255,0.05);
}

.traffic-light {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    margin: 16px auto;

    background:
        radial-gradient(
            circle at 35% 30%,
            #555,
            #181818 60%,
            #050505
        );

    border: 5px solid #333;

    box-shadow:
        inset 0 0 20px #000,
        0 3px 8px rgba(0,0,0,0.6);

    transition: all 0.3s ease;
}

.red-active {
    background:
        radial-gradient(
            circle at 35% 30%,
            #ffaaaa,
            #ff1b1b 45%,
            #9b0000 80%
        );

    box-shadow:
        0 0 12px #ff0000,
        0 0 30px #ff0000,
        0 0 60px rgba(255,0,0,0.85),
        0 0 100px rgba(255,0,0,0.5);
}

.yellow-active {
    background:
        radial-gradient(
            circle at 35% 30%,
            #fff5a0,
            #ffd000 45%,
            #9c7800 80%
        );

    box-shadow:
        0 0 12px #ffd000,
        0 0 30px #ffd000,
        0 0 60px rgba(255,210,0,0.85),
        0 0 100px rgba(255,210,0,0.5);
}

.green-active {
    background:
        radial-gradient(
            circle at 35% 30%,
            #a5ffbe,
            #00df52 45%,
            #00752b 80%
        );

    box-shadow:
        0 0 12px #00ff55,
        0 0 30px #00ff55,
        0 0 60px rgba(0,255,80,0.85),
        0 0 100px rgba(0,255,80,0.5);
}

.signal-name {
    color: white;
    text-align: center;
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 8px;
}

.signal-status {
    text-align: center;
    font-size: 30px;
    font-weight: 900;
    margin-top: 10px;
}

.feature-box {
    background: white;
    padding: 14px;
    border-radius: 12px;
    margin: 6px 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    font-weight: 600;
}

.footer {
    text-align: center;
    padding: 25px;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🚦 TRAFFIC SIGNAL MANAGEMENT SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">20 FEATURES SMART TRAFFIC CONTROL DASHBOARD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="creator">Created By: Rashpreet Kaur Arora</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🚦 Control Panel")

st.sidebar.markdown(
    "**Traffic Signal Management System**"
)

st.sidebar.divider()

st.session_state.running = st.sidebar.toggle(
    "Automatic Signal Mode",
    value=st.session_state.running
)

st.session_state.manual_mode = st.sidebar.toggle(
    "Manual Control",
    value=st.session_state.manual_mode
)

st.session_state.night_mode = st.sidebar.toggle(
    "🌙 Night Traffic Mode",
    value=st.session_state.night_mode
)

st.session_state.school_zone = st.sidebar.toggle(
    "🏫 School Zone Mode",
    value=st.session_state.school_zone
)

st.session_state.pedestrian = st.sidebar.toggle(
    "🚶 Pedestrian Crossing",
    value=st.session_state.pedestrian
)

st.session_state.emergency = st.sidebar.toggle(
    "🚑 Emergency Vehicle",
    value=st.session_state.emergency
)

st.sidebar.divider()

st.sidebar.subheader("Traffic Simulation")

st.session_state.vehicle_count = st.sidebar.slider(
    "Vehicles Detected",
    min_value=0,
    max_value=150,
    value=st.session_state.vehicle_count
)

if st.sidebar.button(
    "🎲 Random Traffic",
    use_container_width=True
):
    st.session_state.vehicle_count = random.randint(5, 150)

if st.sidebar.button(
    "🔄 Reset System",
    use_container_width=True
):
    st.session_state.signal = "RED"
    st.session_state.running = True
    st.session_state.last_change = time.time()
    st.session_state.vehicle_count = 45
    st.session_state.emergency = False
    st.session_state.accident = False
    st.session_state.wrong_way = False


# ============================================================
# ADAPTIVE TRAFFIC LOGIC
# ============================================================

adaptive_timing()

density = calculate_density()


# ============================================================
# EMERGENCY MODE
# ============================================================

if st.session_state.emergency:

    st.session_state.signal = "GREEN"

    st.session_state.last_change = time.time()


# ============================================================
# AUTOMATIC SIGNAL TIMER
# ============================================================

duration = get_duration()

elapsed = int(time.time() - st.session_state.last_change)

remaining = max(duration - elapsed, 0)

if (
    st.session_state.running
    and not st.session_state.manual_mode
    and not st.session_state.emergency
):

    if remaining <= 0:
        next_signal()
        st.rerun()


# ============================================================
# MAIN DASHBOARD
# ============================================================

left, middle, right = st.columns([1, 1.2, 1])


# ============================================================
# LEFT PANEL
# ============================================================

with left:

    st.markdown(
        '<div class="dashboard-card">',
        unsafe_allow_html=True
    )

    st.subheader("📊 Traffic Information")

    st.metric(
        "🚗 Vehicles",
        st.session_state.vehicle_count
    )

    st.metric(
        "Traffic Density",
        density
    )

    st.metric(
        "Current Signal",
        st.session_state.signal
    )

    st.metric(
        "Signal Timer",
        f"{remaining} sec"
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# CENTER TRAFFIC LIGHT
# ============================================================

with middle:

    st.subheader("🚦 Live Traffic Signal")

    red_class = (
        "traffic-light red-active"
        if st.session_state.signal == "RED"
        else "traffic-light"
    )

    yellow_class = (
        "traffic-light yellow-active"
        if st.session_state.signal == "YELLOW"
        else "traffic-light"
    )

    green_class = (
        "traffic-light green-active"
        if st.session_state.signal == "GREEN"
        else "traffic-light"
    )

    signal_html = f"""

    <div class="traffic-body">

        <div class="{red_class}"></div>

        <div class="{yellow_class}"></div>

        <div class="{green_class}"></div>

        <div class="signal-name">
            TRAFFIC SIGNAL
        </div>

    </div>

    <div class="signal-status">
        {signal_color()}
    </div>

    """

    st.markdown(
        signal_html,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="text-align:center;
                    font-size:24px;
                    font-weight:800;">
            ⏱️ {remaining} seconds
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RIGHT CONTROL PANEL
# ============================================================

with right:

    st.markdown(
        '<div class="dashboard-card">',
        unsafe_allow_html=True
    )

    st.subheader("🎛️ Signal Controls")

    if st.button(
        "🔴 RED",
        use_container_width=True
    ):
        st.session_state.signal = "RED"
        st.session_state.last_change = time.time()
        st.rerun()

    if st.button(
        "🟡 YELLOW",
        use_container_width=True
    ):
        st.session_state.signal = "YELLOW"
        st.session_state.last_change = time.time()
        st.rerun()

    if st.button(
        "🟢 GREEN",
        use_container_width=True
    ):
        st.session_state.signal = "GREEN"
        st.session_state.last_change = time.time()
        st.rerun()

    if st.button(
        "🔄 Next Signal",
        use_container_width=True
    ):
        next_signal()
        st.rerun()

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# STATUS
# ============================================================

st.divider()

st.subheader("🛰️ System Status")

status1, status2, status3, status4 = st.columns(4)

with status1:

    if st.session_state.running:
        st.success("System Running")
    else:
        st.warning("System Paused")

with status2:

    if st.session_state.emergency:
        st.error("Emergency Mode")
    else:
        st.success("Normal Mode")

with status3:

    if density == "HIGH":
        st.error("High Traffic")
    elif density == "MEDIUM":
        st.warning("Medium Traffic")
    else:
        st.success("Low Traffic")

with status4:

    if st.session_state.pedestrian:
        st.warning("Pedestrian Active")
    else:
        st.success("Pedestrian Clear")


# ============================================================
# SMART TRAFFIC ANALYSIS
# ============================================================

st.divider()

st.header("🤖 Smart Traffic Analysis")

analysis_col1, analysis_col2 = st.columns(2)

with analysis_col1:

    st.markdown(
        '<div class="dashboard-card">',
        unsafe_allow_html=True
    )

    st.subheader("📈 Traffic Analysis")

    if density == "HIGH":

        st.error(
            "High traffic detected. "
            "Adaptive green time has been increased."
        )

    elif density == "MEDIUM":

        st.warning(
            "Medium traffic detected. "
            "Normal adaptive timing is active."
        )

    else:

        st.success(
            "Low traffic detected. "
            "Signal timing has been reduced."
        )

    st.write(
        f"Detected vehicles: **{st.session_state.vehicle_count}**"
    )

    st.write(
        f"Recommended green time: "
        f"**{st.session_state.green_time} seconds**"
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


with analysis_col2:

    st.markdown(
        '<div class="dashboard-card">',
        unsafe_allow_html=True
    )

    st.subheader("🧠 AI Recommendation")

    if st.session_state.emergency:

        st.info(
            "Emergency vehicle detected. "
            "GREEN priority is recommended."
        )

    elif density == "HIGH":

        st.info(
            "Increase green signal duration "
            "to reduce congestion."
        )

    elif density == "MEDIUM":

        st.info(
            "Maintain adaptive signal timing."
        )

    else:

        st.info(
            "Shorter signal cycles are recommended."
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# EMERGENCY MANAGEMENT
# ============================================================

st.divider()

st.header("🚨 Emergency & Incident Management")

e1, e2, e3 = st.columns(3)

with e1:

    st.session_state.accident = st.checkbox(
        "🚑 Accident Detected",
        value=st.session_state.accident
    )

with e2:

    st.session_state.wrong_way = st.checkbox(
        "⚠️ Wrong-Way Vehicle",
        value=st.session_state.wrong_way
    )

with e3:

    if st.session_state.emergency:
        st.error("🚨 Emergency Priority ACTIVE")
    else:
        st.success("Normal Traffic Priority")


if st.session_state.accident:

    st.error(
        "ACCIDENT ALERT: Traffic management "
        "team should be notified."
    )

if st.session_state.wrong_way:

    st.warning(
        "WRONG-WAY ALERT: Vehicle movement "
        "requires monitoring."
    )


# ============================================================
# PEDESTRIAN CROSSING
# ============================================================

st.divider()

st.header("🚶 Pedestrian Crossing Management")

if st.session_state.pedestrian:

    st.warning(
        "Pedestrian crossing is ACTIVE. "
        "Vehicles should remain stopped."
    )

else:

    st.success(
        "Pedestrian crossing is CLEAR."
    )


# ============================================================
# SCHOOL ZONE
# ============================================================

st.divider()

st.header("🏫 School Zone Traffic Control")

if st.session_state.school_zone:

    st.warning(
        "School Zone Mode ACTIVE — "
        "reduced traffic speed recommended."
    )

else:

    st.success(
        "School Zone Mode is currently OFF."
    )


# ============================================================
# NIGHT MODE
# ============================================================

st.divider()

st.header("🌙 Night Traffic Management")

if st.session_state.night_mode:

    st.info(
        "Night Mode ACTIVE — "
        "low-traffic signal strategy enabled."
    )

else:

    st.success(
        "Day Traffic Mode ACTIVE."
    )


# ============================================================
# 20 FEATURES
# ============================================================

st.divider()

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

feature_col1, feature_col2 = st.columns(2)

for index, feature in enumerate(features):

    if index < 10:

        with feature_col1:

            st.markdown(
                f'<div class="feature-box">'
                f'✅ {index + 1}. {feature}'
                f'</div>',
                unsafe_allow_html=True
            )

    else:

        with feature_col2:

            st.markdown(
                f'<div class="feature-box">'
                f'✅ {index + 1}. {feature}'
                f'</div>',
                unsafe_allow_html=True
            )


# ============================================================
# TRAFFIC STATISTICS
# ============================================================

st.divider()

st.header("📊 Traffic Statistics")

chart_data = {
    "Red": st.session_state.red_time,
    "Yellow": st.session_state.yellow_time,
    "Green": st.session_state.green_time
}

st.bar_chart(chart_data)


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

st.header("📋 Project Information")

info1, info2, info3 = st.columns(3)

with info1:

    st.markdown(
        """
        **Project:**  
        Traffic Signal Management System

        **Technology:**  
        Python + Streamlit
        """
    )

with info2:

    st.markdown(
        """
        **Hardware:**  
        Not Required

        **Features:**  
        20
        """
    )

with info3:

    st.markdown(
        """
        **Developer:**  
        Rashpreet Kaur Arora

        **Application:**  
        Smart Traffic Dashboard
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        🚦 <b>Traffic Signal Management System</b><br>
        20 Features Smart Traffic Control Project<br><br>
        Created By: <b>Rashpreet Kaur Arora</b>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# AUTO REFRESH
# ============================================================

if st.session_state.running and not st.session_state.manual_mode:

    time.sleep(1)

    st.rerun()
