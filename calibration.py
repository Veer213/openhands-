"""
=========================================
OpenHands
calibration.py

Handles hand calibration.

Author : Veer Pratap
=========================================
"""

import math


class Calibration:

    def __init__(self):

        # Left hand neutral position
        self.left_x = None
        self.left_y = None

        # Right hand neutral position
        self.right_x = None
        self.right_y = None

        # Calibration status
        self.calibrated = False

    # -----------------------------------
    # Save neutral hand positions
    # -----------------------------------

    def calibrate(self, tracker):

        if tracker.left_palm is None or tracker.right_palm is None:
            return False

        self.left_x = tracker.left_palm.x
        self.left_y = tracker.left_palm.y

        self.right_x = tracker.right_palm.x
        self.right_y = tracker.right_palm.y

        self.calibrated = True

        print("\n========== CALIBRATED ==========")
        print(f"Left  : ({self.left_x:.3f}, {self.left_y:.3f})")
        print(f"Right : ({self.right_x:.3f}, {self.right_y:.3f})")
        print("================================\n")

        return True

    # -----------------------------------
    # Check calibration
    # -----------------------------------

    def is_calibrated(self):

        return self.calibrated

    # -----------------------------------
    # Left hand offset
    # -----------------------------------

    def left_offset(self, tracker):

        if not self.calibrated:
            return (0.0, 0.0)

        if tracker.left_palm is None:
            return (0.0, 0.0)

        dx = tracker.left_palm.x - self.left_x
        dy = tracker.left_palm.y - self.left_y

        return (dx, dy)

    # -----------------------------------
    # Right hand offset
    # -----------------------------------

    def right_offset(self, tracker):

        if not self.calibrated:
            return (0.0, 0.0)

        if tracker.right_palm is None:
            return (0.0, 0.0)

        dx = tracker.right_palm.x - self.right_x
        dy = tracker.right_palm.y - self.right_y

        return (dx, dy)

    # -----------------------------------
    # Distance from center
    # -----------------------------------

    def left_distance(self, tracker):

        dx, dy = self.left_offset(tracker)

        return math.sqrt(dx * dx + dy * dy)

    def right_distance(self, tracker):

        dx, dy = self.right_offset(tracker)

        return math.sqrt(dx * dx + dy * dy)

    # -----------------------------------
    # Reset calibration
    # -----------------------------------

    def reset(self):

        self.left_x = None
        self.left_y = None

        self.right_x = None
        self.right_y = None

        self.calibrated = False

        print("Calibration Reset")