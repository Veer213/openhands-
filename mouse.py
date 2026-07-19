"""
=========================================
OpenHands
mouse.py

Controls the Windows mouse.

Features
- Relative Mouse Movement
- Smoothing
- Dead Zone
- Sensitivity
=========================================
"""

import ctypes


class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_long),
        ("y", ctypes.c_long)
    ]


class MouseController:

    def __init__(self):

        # Previous finger position
        self.prev_x = None
        self.prev_y = None

        # Settings
        self.sensitivity = 2.0
        self.deadzone = 0.005

        # Smoothing
        self.smooth_dx = 0
        self.smooth_dy = 0

        self.alpha = 0.30

    def move_relative(self, dx, dy):

        ctypes.windll.user32.mouse_event(
            0x0001,
            int(dx),
            int(dy),
            0,
            0
        )

    def update(self, right_hand):

        if right_hand is None:

            self.prev_x = None
            self.prev_y = None
            return

        # Index Finger Tip
        finger = right_hand.landmark[8]

        x = finger.x
        y = finger.y

        # First frame
        if self.prev_x is None:

            self.prev_x = x
            self.prev_y = y
            return

        # Delta
        dx = x - self.prev_x
        dy = y - self.prev_y

        self.prev_x = x
        self.prev_y = y

        # Dead zone
        if abs(dx) < self.deadzone:
            dx = 0

        if abs(dy) < self.deadzone:
            dy = 0

        # Sensitivity
        dx *= 1000 * self.sensitivity
        dy *= 1000 * self.sensitivity

        # Exponential smoothing
        self.smooth_dx = (
            self.alpha * dx
            + (1 - self.alpha) * self.smooth_dx
        )

        self.smooth_dy = (
            self.alpha * dy
            + (1 - self.alpha) * self.smooth_dy
        )

        # Move mouse
        self.move_relative(
            self.smooth_dx,
            self.smooth_dy
        )