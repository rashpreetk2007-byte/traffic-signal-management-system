from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# ============================================================
# TRAFFIC SIGNAL MANAGEMENT SYSTEM - FLASK API
# Created By: Rashpreet Kaur Arora
# 20 FEATURES PROJECT
# ============================================================

signal_data = {
    "signal": "RED",
    "vehicle_count": 45,
    "traffic_density": "MEDIUM",

    "emergency": False,
    "pedestrian": False,
    "accident": False,
    "wrong_way": False,

    "school_zone": False,
    "night_mode": False,
    "manual_mode": False,

    "green_time": 12,
    "yellow_time": 4,
    "red_time": 10,

    "system_status": "RUNNING"
}

last_change = time.time()


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return jsonify({
        "project": "Traffic Signal Management System",
        "created_by": "Rashpreet Kaur Arora",
        "features": 20,
        "technology": "Python + Flask API",
        "status": "ONLINE",
        "message": "Flask API is working successfully"
    })


# ============================================================
# SIGNAL STATUS
# ============================================================

@app.route("/api/status")
def status():

    data = signal_data.copy()

    data["elapsed"] = int(time.time() - last_change)

    return jsonify(data)


# ============================================================
# GET CURRENT SIGNAL
# ============================================================

@app.route("/api/signal")
def get_signal():

    return jsonify({
        "signal": signal_data["signal"],
        "status": "ACTIVE"
    })


# ============================================================
# CHANGE SIGNAL
# ============================================================

@app.route("/api/signal/<signal>")
def change_signal(signal):

    global last_change

    signal = signal.upper()

    if signal not in ["RED", "YELLOW", "GREEN"]:

        return jsonify({
            "success": False,
            "error": "Invalid signal. Use RED, YELLOW or GREEN."
        }), 400

    signal_data["signal"] = signal

    last_change = time.time()

    return jsonify({
        "success": True,
        "signal": signal,
        "message": f"{signal} signal activated"
    })


# ============================================================
# RED SIGNAL
# ============================================================

@app.route("/api/red")
def red_signal():

    global last_change

    signal_data["signal"] = "RED"

    last_change = time.time()

    return jsonify({
        "success": True,
        "signal": "RED"
    })


# ============================================================
# YELLOW SIGNAL
# ============================================================

@app.route("/api/yellow")
def yellow_signal():

    global last_change

    signal_data["signal"] = "YELLOW"

    last_change = time.time()

    return jsonify({
        "success": True,
        "signal": "YELLOW"
    })


# ============================================================
# GREEN SIGNAL
# ============================================================

@app.route("/api/green")
def green_signal():

    global last_change

    signal_data["signal"] = "GREEN"

    last_change = time.time()

    return jsonify({
        "success": True,
        "signal": "GREEN"
    })


# ============================================================
# VEHICLE COUNT
# ============================================================

@app.route("/api/vehicles", methods=["GET", "POST"])
def vehicles():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        count = data.get("count")

        if count is None:

            return jsonify({
                "success": False,
                "error": "Vehicle count is required"
            }), 400

        try:
            count = int(count)

        except:

            return jsonify({
                "success": False,
                "error": "Vehicle count must be a number"
            }), 400

        if count < 0:

            count = 0

        signal_data["vehicle_count"] = count

        update_density()

    return jsonify({
        "vehicle_count": signal_data["vehicle_count"],
        "traffic_density": signal_data["traffic_density"]
    })


# ============================================================
# TRAFFIC DENSITY
# ============================================================

def update_density():

    count = signal_data["vehicle_count"]

    if count < 30:

        signal_data["traffic_density"] = "LOW"

    elif count < 70:

        signal_data["traffic_density"] = "MEDIUM"

    else:

        signal_data["traffic_density"] = "HIGH"


# ============================================================
# ADAPTIVE SIGNAL TIMING
# ============================================================

@app.route("/api/adaptive-timing")
def adaptive_timing():

    count = signal_data["vehicle_count"]

    if count >= 90:

        green = 20

    elif count >= 70:

        green = 16

    elif count >= 40:

        green = 12

    else:

        green = 8

    signal_data["green_time"] = green

    return jsonify({
        "vehicle_count": count,
        "traffic_density": signal_data["traffic_density"],
        "recommended_green_time": green,
        "unit": "seconds"
    })


# ============================================================
# EMERGENCY MODE
# ============================================================

@app.route("/api/emergency", methods=["GET", "POST"])
def emergency():

    global last_change

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        enabled = data.get("enabled", True)

        signal_data["emergency"] = bool(enabled)

        if signal_data["emergency"]:

            signal_data["signal"] = "GREEN"
            last_change = time.time()

    return jsonify({
        "emergency": signal_data["emergency"],
        "signal": signal_data["signal"]
    })


# ============================================================
# PEDESTRIAN MODE
# ============================================================

@app.route("/api/pedestrian", methods=["GET", "POST"])
def pedestrian():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        signal_data["pedestrian"] = bool(
            data.get("enabled", True)
        )

    return jsonify({
        "pedestrian": signal_data["pedestrian"]
    })


# ============================================================
# ACCIDENT ALERT
# ============================================================

@app.route("/api/accident", methods=["GET", "POST"])
def accident():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        signal_data["accident"] = bool(
            data.get("detected", True)
        )

    return jsonify({
        "accident_detected": signal_data["accident"]
    })


# ============================================================
# WRONG WAY ALERT
# ============================================================

@app.route("/api/wrong-way", methods=["GET", "POST"])
def wrong_way():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        signal_data["wrong_way"] = bool(
            data.get("detected", True)
        )

    return jsonify({
        "wrong_way_detected": signal_data["wrong_way"]
    })


# ============================================================
# SCHOOL ZONE
# ============================================================

@app.route("/api/school-zone", methods=["GET", "POST"])
def school_zone():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        signal_data["school_zone"] = bool(
            data.get("enabled", True)
        )

    return jsonify({
        "school_zone": signal_data["school_zone"]
    })


# ============================================================
# NIGHT MODE
# ============================================================

@app.route("/api/night-mode", methods=["GET", "POST"])
def night_mode():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        signal_data["night_mode"] = bool(
            data.get("enabled", True)
        )

    return jsonify({
        "night_mode": signal_data["night_mode"]
    })


# ============================================================
# MANUAL MODE
# ============================================================

@app.route("/api/manual-mode", methods=["GET", "POST"])
def manual_mode():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        signal_data["manual_mode"] = bool(
            data.get("enabled", True)
        )

    return jsonify({
        "manual_mode": signal_data["manual_mode"]
    })


# ============================================================
# SYSTEM HEALTH
# ============================================================

@app.route("/api/health")
def health():

    return jsonify({
        "status": "OK",
        "flask": "RUNNING",
        "port": 5050,
        "api": "ONLINE"
    })


# ============================================================
# RESET SYSTEM
# ============================================================

@app.route("/api/reset", methods=["POST"])
def reset():

    global last_change

    signal_data["signal"] = "RED"
    signal_data["vehicle_count"] = 45
    signal_data["traffic_density"] = "MEDIUM"

    signal_data["emergency"] = False
    signal_data["pedestrian"] = False
    signal_data["accident"] = False
    signal_data["wrong_way"] = False

    signal_data["school_zone"] = False
    signal_data["night_mode"] = False
    signal_data["manual_mode"] = False

    signal_data["green_time"] = 12
    signal_data["yellow_time"] = 4
    signal_data["red_time"] = 10

    last_change = time.time()

    return jsonify({
        "success": True,
        "message": "Traffic management system reset successfully",
        "signal": "RED"
    })


# ============================================================
# RUN FLASK
# ============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("TRAFFIC SIGNAL MANAGEMENT SYSTEM")
    print("Created By: Rashpreet Kaur Arora")
    print("20 FEATURES PROJECT")
    print("Flask API Port: 5050")
    print("=" * 50)

    app.run(
        host="0.0.0.0",
        port=5050,
        debug=False,
        use_reloader=False
      )
