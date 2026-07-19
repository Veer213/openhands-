"""
=========================================
OpenHands
ui.py

Draws the OpenHands HUD

Author : Veer Pratap
=========================================
"""

import cv2
from config import *


class UI:

    def __init__(self):
        pass

    # =========================================
    # Draw Text
    # =========================================

    def text(self, frame, text, x, y, color=WHITE):

        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            FONT_SCALE,
            color,
            LINE_THICKNESS
        )

    # =========================================
    # Top Bar
    # =========================================

    def draw_top(self, frame, fps):

        cv2.rectangle(
            frame,
            (0, 0),
            (frame.shape[1], 60),
            (35, 35, 35),
            -1
        )

        self.text(frame, "OpenHands", 20, 40, GREEN)
        self.text(frame, f"FPS : {int(fps)}", 220, 40)

    # =========================================
    # Left Movement Guide
    # =========================================

    def draw_left_panel(self, frame):

        x = 20
        y = 90

        width = 340
        height = 500

        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            CYAN,
            3
        )

        self.text(frame, "LEFT HAND", x + 90, y + 35)

        self.text(frame, "Movement Guide", x + 60, y + 70)

        cx = x + width // 2
        cy = y + 220

        # Outer Circle
        cv2.circle(
            frame,
            (cx, cy),
            100,
            WHITE,
            2
        )

        # Dead Zone
        cv2.circle(
            frame,
            (cx, cy),
            35,
            GREEN,
            2
        )

        cv2.circle(
            frame,
            (cx, cy),
            6,
            GREEN,
            -1
        )

        # Direction Arrows
        cv2.arrowedLine(frame, (cx, cy), (cx, cy - 80), WHITE, 2)
        cv2.arrowedLine(frame, (cx, cy), (cx - 80, cy), WHITE, 2)
        cv2.arrowedLine(frame, (cx, cy), (cx + 80, cy), WHITE, 2)
        cv2.arrowedLine(frame, (cx, cy), (cx, cy + 80), WHITE, 2)

        # WASD
        self.text(frame, "W", cx - 10, cy - 105)
        self.text(frame, "A", cx - 110, cy + 5)
        self.text(frame, "D", cx + 90, cy + 5)
        self.text(frame, "S", cx - 10, cy + 120)

        self.text(frame, "Keep Palm In Green Circle", x + 25, y + 380)

        self.text(frame, "Move Palm Towards W A S D", x + 15, y + 420)

        self.text(frame, "Movement activates outside deadzone", x + 5, y + 460)

    # =========================================
    # Right Gesture Guide
    # =========================================

    def draw_right_panel(self, frame, gesture):

        x = frame.shape[1] - 300
        y = 90

        width = 260
        height = 340

        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            CYAN,
            3
        )

        self.text(frame, "RIGHT HAND", x + 55, y + 35)

        self.text(frame, "👌 Shoot", x + 20, y + 80,
                  GREEN if gesture == "SHOOT" else WHITE)

        self.text(frame, "✌ ADS", x + 20, y + 125,
                  GREEN if gesture == "ADS" else WHITE)

        self.text(frame, "✊ Reload", x + 20, y + 170,
                  GREEN if gesture == "RELOAD" else WHITE)

        self.text(frame, "☝ Jump", x + 20, y + 215,
                  GREEN if gesture == "JUMP" else WHITE)

        self.text(frame, "Current", x + 20, y + 280)

        self.text(frame, gesture, x + 130, y + 280, GREEN)

    # =========================================
    # Mouse Zone
    # =========================================

    def draw_mouse_box(self, frame):

        cx = frame.shape[1] // 2
        cy = frame.shape[0] // 2

        size = 90

        cv2.rectangle(
            frame,
            (cx - size, cy - size),
            (cx + size, cy + size),
            BLUE,
            2
        )

        cv2.circle(
            frame,
            (cx, cy),
            6,
            GREEN,
            -1
        )

        self.text(frame, "LOOK", cx - 25, cy - 105)

        self.text(frame, "Neutral", cx - 35, cy + 120)

    # =========================================
    # Status
    # =========================================

    def draw_status(self, frame, tracker):

        left = "FOUND" if tracker.left_hand else "NOT FOUND"
        right = "FOUND" if tracker.right_hand else "NOT FOUND"

        self.text(
            frame,
            f"Left : {left}",
            20,
            frame.shape[0] - 35,
            GREEN if tracker.left_hand else RED
        )

        self.text(
            frame,
            f"Right : {right}",
            260,
            frame.shape[0] - 35,
            GREEN if tracker.right_hand else RED
        )

    # =========================================
    # Main Draw
    # =========================================

    def draw(self, frame, tracker, gesture, mouse, movement, fps):

        self.draw_top(frame, fps)

        self.draw_left_panel(frame)

        self.draw_right_panel(frame, gesture)

        self.draw_mouse_box(frame)

        self.draw_status(frame, tracker)

        return frame