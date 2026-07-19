"""
=========================================
OpenHands
gestures.py

Gesture Recognition Engine

Supported Gestures

- IDLE
- SHOOT
- ADS
- RELOAD
- JUMP
=========================================
"""


class GestureController:

    def __init__(self):

        self.current_gesture = "IDLE"

    # ----------------------------
    # Distance between two fingers
    # ----------------------------
    def distance(self, p1, p2):

        dx = p1.x - p2.x
        dy = p1.y - p2.y

        return (dx * dx + dy * dy) ** 0.5

    # ----------------------------
    # Finger Extended?
    # ----------------------------
    def finger_up(self, tip, pip):

        return tip.y < pip.y

    # ----------------------------
    # Update Gesture
    # ----------------------------
    def update(self, hand):

        if hand is None:

            self.current_gesture = "IDLE"
            return self.current_gesture

        lm = hand.landmark

        thumb_tip = lm[4]

        index_tip = lm[8]
        index_pip = lm[6]

        middle_tip = lm[12]
        middle_pip = lm[10]

        ring_tip = lm[16]
        ring_pip = lm[14]

        pinky_tip = lm[20]
        pinky_pip = lm[18]

        # ----------------------------
        # Finger States
        # ----------------------------

        index = self.finger_up(index_tip, index_pip)
        middle = self.finger_up(middle_tip, middle_pip)
        ring = self.finger_up(ring_tip, ring_pip)
        pinky = self.finger_up(pinky_tip, pinky_pip)

        # ----------------------------
        # SHOOT
        # Thumb + Index Pinch
        # ----------------------------

        if self.distance(thumb_tip, index_tip) < 0.05:

            self.current_gesture = "SHOOT"
            return self.current_gesture

        # ----------------------------
        # ADS
        # Thumb + Middle Pinch
        # ----------------------------

        if self.distance(thumb_tip, middle_tip) < 0.05:

            self.current_gesture = "ADS"
            return self.current_gesture

        # ----------------------------
        # RELOAD
        # Closed Fist
        # ----------------------------

        if (not index and
            not middle and
            not ring and
            not pinky):

            self.current_gesture = "RELOAD"
            return self.current_gesture

        # ----------------------------
        # JUMP
        # Peace Sign
        # ----------------------------

        if (index and
            middle and
            not ring and
            not pinky):

            self.current_gesture = "JUMP"
            return self.current_gesture

        self.current_gesture = "IDLE"

        return self.current_gesture