"""
=========================================
OpenHands
movement.py

Movement Detection

Author : Veer Pratap
=========================================
"""

class MovementController:

    def __init__(self):

        # Deadzone
        self.deadzone = 0.06

        # Current movement
        self.current_direction = "IDLE"

        self.forward = False
        self.backward = False
        self.left = False
        self.right = False

    # =====================================

    def update(self, tracker, calibration):

        self.current_direction = "IDLE"

        self.forward = False
        self.backward = False
        self.left = False
        self.right = False

        if not calibration.is_calibrated():
            return

        dx, dy = calibration.left_offset(tracker)

        # ------------------------------
        # Horizontal
        # ------------------------------

        if dx < -self.deadzone:
            self.left = True

        elif dx > self.deadzone:
            self.right = True

        # ------------------------------
        # Vertical
        # ------------------------------

        if dy < -self.deadzone:
            self.forward = True

        elif dy > self.deadzone:
            self.backward = True

        # ------------------------------
        # Build Direction String
        # ------------------------------

        direction = ""

        if self.forward:
            direction += "W"

        if self.backward:
            direction += "S"

        if self.left:
            direction += "A"

        if self.right:
            direction += "D"

        if direction == "":
            direction = "IDLE"

        self.current_direction = direction

    # =====================================

    def get_direction(self):

        return self.current_direction
    