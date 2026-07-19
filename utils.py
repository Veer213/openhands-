"""
=========================================
OpenHands
utils.py

Utility functions and helper classes

Author : Veer Pratap
=========================================
"""

import math
import time


# =====================================================
# Console
# =====================================================

def print_header():

    print("=" * 50)
    print("OpenHands")
    print("AI Hand Tracking FPS Controller")
    print("Version 0.2")
    print("=" * 50)


# =====================================================
# FPS Counter
# =====================================================

class FPSCounter:

    def __init__(self):

        self.previous_time = time.time()
        self.fps = 0

    def update(self):

        current_time = time.time()

        delta = current_time - self.previous_time

        self.previous_time = current_time

        if delta > 0:
            self.fps = 1 / delta

        return int(self.fps)


# =====================================================
# Math
# =====================================================

def clamp(value, minimum, maximum):

    return max(minimum, min(value, maximum))


def lerp(start, end, alpha):

    return start + (end - start) * alpha


def map_value(value,
              input_min,
              input_max,
              output_min,
              output_max):

    if input_max == input_min:
        return output_min

    return (
        (value - input_min)
        * (output_max - output_min)
        / (input_max - input_min)
    ) + output_min


# =====================================================
# Landmark Utilities
# =====================================================

def distance(point1, point2):

    return math.sqrt(
        (point1.x - point2.x) ** 2 +
        (point1.y - point2.y) ** 2
    )


def midpoint(point1, point2):

    x = (point1.x + point2.x) / 2
    y = (point1.y + point2.y) / 2

    return x, y


def landmark_to_pixel(landmark, frame):

    height, width = frame.shape[:2]

    x = int(landmark.x * width)
    y = int(landmark.y * height)

    return x, y


# =====================================================
# Finger Detection
# =====================================================

def finger_up(tip, pip):

    return tip.y < pip.y


# =====================================================
# Smoothing
# =====================================================

class SmoothValue:

    def __init__(self, alpha=0.3):

        self.alpha = alpha
        self.value = 0

    def update(self, new_value):

        self.value = lerp(
            self.value,
            new_value,
            self.alpha
        )

        return self.value


# =====================================================
# Vector2
# =====================================================

class Vector2:

    def __init__(self, x=0.0, y=0.0):

        self.x = x
        self.y = y

    def length(self):

        return math.sqrt(
            self.x ** 2 +
            self.y ** 2
        )

    def normalize(self):

        l = self.length()

        if l == 0:
            return Vector2()

        return Vector2(
            self.x / l,
            self.y / l
        )

    def __add__(self, other):

        return Vector2(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):

        return Vector2(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, value):

        return Vector2(
            self.x * value,
            self.y * value
        )

    def __repr__(self):

        return f"Vector2({self.x:.2f}, {self.y:.2f})"


# =====================================================
# Drawing Helpers
# =====================================================

def draw_point(frame, x, y, color=(0, 255, 0), radius=5):

    import cv2

    cv2.circle(
        frame,
        (int(x), int(y)),
        radius,
        color,
        -1
    )


def draw_line(frame, p1, p2, color=(255, 255, 255), thickness=2):

    import cv2

    cv2.line(
        frame,
        (int(p1[0]), int(p1[1])),
        (int(p2[0]), int(p2[1])),
        color,
        thickness
    )


# =====================================================
# End of File
# =====================================================