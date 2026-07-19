"""
=========================================
OpenHands
config.py

Global Settings

Change values here instead of editing
the code.
=========================================
"""

# =========================================
# CAMERA
# =========================================

CAMERA_ID = 0

CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

# =========================================
# TRACKING
# =========================================

MAX_HANDS = 2

MIN_DETECTION_CONFIDENCE = 0.70
MIN_TRACKING_CONFIDENCE = 0.70

# =========================================
# MOUSE
# =========================================

MOUSE_SENSITIVITY = 2.0

MOUSE_SMOOTHING = 0.30

MOUSE_DEADZONE = 0.005

MOUSE_SPEED = 1000

# =========================================
# MOVEMENT
# =========================================

MOVEMENT_DEADZONE = 0.05

# =========================================
# GESTURES
# =========================================

PINCH_DISTANCE = 0.05

ADS_DISTANCE = 0.05

# =========================================
# DEBUG
# =========================================

SHOW_FPS = True

SHOW_HAND_LABELS = True

SHOW_HAND_LANDMARKS = True

SHOW_DEBUG = True

SHOW_GESTURE = True

SHOW_JOYSTICK = True

SHOW_MOUSE_BOX = True

# =========================================
# COLORS
# OpenCV uses BGR
# =========================================

GREEN = (0,255,0)

RED = (0,0,255)

BLUE = (255,0,0)

WHITE = (255,255,255)

YELLOW = (0,255,255)

CYAN = (255,255,0)

MAGENTA = (255,0,255)

# =========================================
# UI
# =========================================

FONT_SCALE = 0.7

LINE_THICKNESS = 2

WINDOW_NAME = "OpenHands"

# =========================================
# FUTURE
# =========================================

ENABLE_SOUND = False

ENABLE_GAME_PROFILES = False

ENABLE_AUTO_CALIBRATION = False