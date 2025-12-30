"""
Global constants for Sports-AI platform
All values are chosen for elite endurance & speed-skating athletes
"""

# -----------------------------
# Physiological limits
# -----------------------------
MIN_HEART_RATE = 30
MAX_HEART_RATE = 230

MIN_SPEED = 0.0          # m/s
MAX_SPEED = 15.0         # m/s (elite skating upper bound)

MIN_CADENCE = 0
MAX_CADENCE = 200

# -----------------------------
# Geometry & sport specifics
# -----------------------------
DEFAULT_LAP_DISTANCE = 400.0  # meters (speed skating rink)

# -----------------------------
# Smoothing / signal processing
# -----------------------------
DEFAULT_SMOOTHING_WINDOW = 5

# -----------------------------
# Training load / fatigue
# -----------------------------
ACWR_SAFE_MIN = 0.8
ACWR_SAFE_MAX = 1.3

# -----------------------------
# Scoring defaults
# -----------------------------
DEFAULT_READINESS_NEUTRAL = 0.5
