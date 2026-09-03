import streamlit as st
import time
import random

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

if "running" not in st.session_state:
    st.session_state.running = True

if "last_change" not in st.session_state:
    st.session_state.last_change = time.time()

if "vehicle_count" not in st.session_state:
    st.session_state.vehicle_count = 45

if "emergency" not in st.session_state:
    st.session_state.emergency = False

if "pedestrian" not in st.session_state:
    st.session_state.pedestrian = False

if "night_mode" not in st.session_state:
    st.session_state.night_mode = False

if "school_zone" not in st.session_state:
    st.session_state.school_zone = False


# ============================================================
# SIGNAL TIMING
# ============================================================

RED_TIME = 10
YELLOW_TIME = 4
GREEN_TIME = 10


def get_time():

    if st.session_state.signal == "RED":
        return RED_TIME

    if st.session_state.signal == "YELLOW":
        return YELLOW_TIME

    return GREEN_TIME


def next_signal():

    if st.session_state.signal == "RED":
        st.session_state.signal = "GREEN"

    elif st.session_state.signal == "GREEN":
        st.session_state.signal = "YELLOW"

    else:
        st.session_state.signal = "RED"

    st.session_state.last_change = time.time()


# ============================================================
# AUTOMATIC SIGNAL
# ============================================================

duration = get_time()

elapsed = int(time.time() - st.session_state.last_change)

remaining = max(duration - elapsed, 0)

if st.session_state.running and not st.session_state.emergency:

    if remaining <= 0:
        next_signal()
        st.rerun()


# ============================================================
# ACTIVE CLASS
# ============================================================

red_active = ""
yellow_active = ""
green_active = ""

if st.session_state.signal == "RED":
    red_active = "active"

elif st.session_state.signal == "YELLOW":
    yellow_active = "active"

else:
    green_active = "active"


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

body {
    background-color: #eef2f7;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 20px;
}

/* =========================================================
   TRAFFIC SIGNAL OUTER BODY
   ========================================================= */

.traffic-container {

    display: flex;
    justify-content: center;
    align-items: center;

    margin-top: 10px;
    margin-bottom: 15px;
}

.traffic-box {

    width: 210px;

    background: linear-gradient(
        145deg,
        #050505,
        #202020,
        #080808
    );

    border: 7px solid #444;

    border-radius: 35px;

    padding: 18px 20px 25px 20px;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.45),
        inset 0 0 20px rgba(255,255,255,0.08);
}

/* =========================================================
   SIMPLE LIGHT SYSTEM
   ========================================================= */

.light {

    text-align: center;

    margin: 7px 0;

    padding: 3px;

}

.circle {

    width: 92px;
    height: 92px;

    margin: auto;

    border-radius: 50%;

    display: flex;
    justify-content: center;
    align-items: center;

    font-size: 70px;

    line-height: 92px;

    color: #222;

    background: #151515;

    border: 5px solid #333;

    box-shadow:
        inset 0 0 18px #000;
}

/* =========================================================
   RED
   ========================================================= */

.circle.red {
    color: #350000;
}

.light.active .circle.red {

    color: #ff2020;

    background:
        radial-gradient(
            circle,
            #ffb0b0 0%,
            #ff2222 38%,
            #a80000 72%,
            #420000 100%
        );

    box-shadow:
        0 0 15px #ff0000,
        0 0 35px #ff0000,
        0 0 65px rgba(255,0,0,0.8);
}

/* =========================================================
   YELLOW
   ========================================================= */

.circle.yellow {
    color: #3d3500;
}

.light.active .circle.yellow {

    color: #ffe600;

    background:
        radial-gradient(
            circle,
            #fff9a0 0%,
            #ffe000 38%,
            #b18c00 72%,
            #4a3900 100%
        );

    box-shadow:
        0 0 15px #ffd900,
        0 0 35px #ffd900,
        0 0 65px rgba(255,210,0,0.8);
}

/* =========================================================
   GREEN
   ========================================================= */

.circle.green {
    color: #003d18;
}

.light.active .circle.green {

    color: #00ff5a;

    background:
        radial-gradient(
            circle,
            #b5ffc9 0%,
            #00ed55 38%,
            #008c35 72%,
            #003d18 100%
        );

    box-shadow:
        0 0 15px #00ff55,
        0 0 35px #00ff55,
        0 0 65px rgba(0,255,80,0.8);
}

/* =========================================================
   LABEL
   ========================================================= */

.light-name {

    color: #aaa;

    font-size: 13px;

    font-weight: 800;

    letter-spacing: 2px;

    margin-top: 2px;
}

.light.active .light-name {

    color: white;

    font-weight: 900;
}

/* =========================================================
   STATUS
   ========================================================= */

.signal-status {

    text-align: center;

    font-size: 30px;

    font-weight: 900;

    margin-top: 8px;
}

.countdown {

    text-align: center;

    font-size: 22px;

    font-weight: 800;

    margin-bottom: 10px;
}

.card {

    background: white;

    border-radius: 18px;

    padding: 18px;

    margin-bottom: 15px;

    box-shadow:
        0 4px 18px rgba(0,0,0,0.08);
}

.feature {

    background: white;

    padding: 12px;

    margin: 5px 0;

    border-radius: 10px;

    font-weight: 600;

    box-shadow:
        0 2px 8px rgba(0,0,0,0.05);
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
    '<div class="subtitle">'
    '20 FEATURES SMART TRAFFIC CONTROL DASHBOARD'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="text-align:center;font-weight:700;">'
    'Created By: Rashpreet Kaur Arora'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🚦 Control Panel")

st.session_state.running = st.sidebar.toggle(
    "Automatic Signal",
    value=st.session_state.running
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

st.session_state.vehicle_count = st.sidebar.slider(
    "🚗 Vehicles Detected",
    0,
    150,
    st.session_state.vehicle_count
)

if st.sidebar.button("🎲 Random Traffic", use_container_width=True):

    st.session_state.vehicle_count = random.randint(5, 150)

    st.rerun()

if st.sidebar.button("🔄 Reset", use_container_width=True):

    st.session_state.signal = "RED"
    st.session_state.last_change = time.time()
    st.session_state.vehicle_count = 45
    st.session_state.emergency = False
    st.session_state.pedestrian = False

    st.rerun()


# ============================================================
# MAIN LAYOUT
# ============================================================

left, center, right = st.columns([1, 1.3, 1])


# ============================================================
# LEFT
# ============================================================

with left:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("📊 Traffic Information")

    count = st.session_state.vehicle_count

    if count < 30:
        density = "LOW"

    elif count < 70:
        density = "MEDIUM"

    else:
        density = "HIGH"

    st.metric("🚗 Vehicles", count)

    st.metric("Traffic Density", density)

    st.metric(
        "Current Signal",
        st.session_state.signal
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CENTER - TRAFFIC LIGHT
# ============================================================

with center:

    st.markdown(
        """
        <div style="
        text-align:center;
        font-size:24px;
        font-weight:900;">
        🚦 LIVE TRAFFIC SIGNAL
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="traffic-container">

            <div class="traffic-box">

                <div class="light {red_active}">
                    <div class="circle red">●</div>
                    <div class="light-name">RED</div>
                </div>

                <div class="light {yellow_active}">
                    <div class="circle yellow">●</div>
                    <div class="light-name">YELLOW</div>
                </div>

                <div class="light {green_active}">
                    <div class="circle green">●</div>
                    <div class="light-name">GREEN</div>
                </div>

            </div>

        </div>

        <div class="signal-status">
            {st.session_state.signal}
        </div>

        <div class="countdown">
            ⏱️ {remaining} seconds
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RIGHT - MANUAL CONTROL
# ============================================================

with right:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🎛️ Signal Control")

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
        "🔄 NEXT SIGNAL",
        use_container_width=True
    ):

        next_signal()

        st.rerun()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SYSTEM STATUS
# ============================================================

st.divider()

st.header("🛰️ System Status")

a, b, c, d = st.columns(4)

with a:

    if st.session_state.running:
        st.success("SYSTEM RUNNING")
    else:
        st.warning("SYSTEM PAUSED")

with b:

    if st.session_state.emergency:
        st.error("EMERGENCY ACTIVE")
    else:
        st.success("NORMAL MODE")

with c:

    if density == "HIGH":
        st.error("HIGH TRAFFIC")

    elif density == "MEDIUM":
        st.warning("MEDIUM TRAFFIC")

    else:
        st.success("LOW TRAFFIC")

with d:

    if st.session_state.pedestrian:
        st.warning("PEDESTRIAN ACTIVE")
    else:
        st.success("ROAD CLEAR")


# ============================================================
# SMART ANALYSIS
# ============================================================

st.divider()

st.header("🤖 Smart Traffic Analysis")

x, y = st.columns(2)

with x:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("📈 Traffic Analysis")

    st.write(
        f"Vehicles detected: **{count}**"
    )

    st.write(
        f"Traffic density: **{density}**"
    )

    if density == "HIGH":

        st.error(
            "High traffic detected. "
            "Green signal duration should be increased."
        )

    elif density == "MEDIUM":

        st.warning(
            "Medium traffic detected. "
            "Adaptive timing is recommended."
        )

    else:

        st.success(
            "Low traffic detected. "
            "Normal signal timing is sufficient."
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


with y:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🧠 Intelligent Recommendation")

    if st.session_state.emergency:

        st.info(
            "Emergency vehicle priority active. "
            "GREEN signal is recommended."
        )

    elif st.session_state.pedestrian:

        st.info(
            "Pedestrian crossing active. "
            "Vehicle movement should be controlled."
        )

    elif density == "HIGH":

        st.info(
            "Heavy congestion detected. "
            "Extend GREEN phase."
        )

    else:

        st.info(
            "Traffic conditions are normal."
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
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

f1, f2 = st.columns(2)

for i, feature in enumerate(features):

    if i < 10:

        with f1:

            st.markdown(
                f"""
                <div class="feature">
                ✅ {i + 1}. {feature}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        with f2:

            st.markdown(
                f"""
                <div class="feature">
                ✅ {i + 1}. {feature}
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

st.header("📋 Project Information")

p1, p2, p3 = st.columns(3)

with p1:

    st.write("**Project**")
    st.write("Traffic Signal Management System")

with p2:

    st.write("**Technology**")
    st.write("Python + Streamlit")

with p3:

    st.write("**Hardware**")
    st.write("Not Required")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    🚦 <b>Traffic Signal Management System</b><br>

    20 Features Smart Traffic Control Project<br>

    Created By: <b>Rashpreet Kaur Arora</b>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# AUTO REFRESH
# ============================================================

if st.session_state.running:

    time.sleep(1)

    st.rerun()
