"""
=========================================
OpenHands
tracker.py

Hand Tracking Engine

Author : Veer Pratap
=========================================
"""

import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self, camera_index=0):

        # =====================================
        # Camera
        # =====================================

        self.cap = cv2.VideoCapture(camera_index)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open webcam.")

        # =====================================
        # MediaPipe
        # =====================================

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            model_complexity=1,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        # =====================================
        # Hand Objects
        # =====================================

        self.left_hand = None
        self.right_hand = None

        self.left_landmarks = None
        self.right_landmarks = None

        self.left_palm = None
        self.right_palm = None

        self.left_index = None
        self.right_index = None

        self.left_palm_px = None
        self.right_palm_px = None

        self.frame_width = 1280
        self.frame_height = 720

    # =========================================

    def update(self):

        success, frame = self.cap.read()

        if not success:
            return None

        frame = cv2.flip(frame, 1)

        self.frame_height, self.frame_width = frame.shape[:2]

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        # Reset every frame
        self.left_hand = None
        self.right_hand = None

        self.left_landmarks = None
        self.right_landmarks = None

        self.left_palm = None
        self.right_palm = None

        self.left_index = None
        self.right_index = None

        self.left_palm_px = None
        self.right_palm_px = None

        if results.multi_hand_landmarks and results.multi_handedness:

            for landmarks, handedness in zip(
                    results.multi_hand_landmarks,
                    results.multi_handedness):

                label = handedness.classification[0].label

                palm = landmarks.landmark[0]
                index = landmarks.landmark[8]

                palm_px = (
                    int(palm.x * self.frame_width),
                    int(palm.y * self.frame_height)
                )

                index_px = (
                    int(index.x * self.frame_width),
                    int(index.y * self.frame_height)
                )

                if label == "Left":

                    self.left_hand = landmarks
                    self.left_landmarks = landmarks

                    self.left_palm = palm
                    self.left_index = index

                    self.left_palm_px = palm_px

                else:

                    self.right_hand = landmarks
                    self.right_landmarks = landmarks

                    self.right_palm = palm
                    self.right_index = index

                    self.right_palm_px = palm_px

                # Draw skeleton
                self.mp_draw.draw_landmarks(
                    frame,
                    landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                # Palm
                cv2.circle(
                    frame,
                    palm_px,
                    10,
                    (0, 255, 0),
                    -1
                )

                # Index Finger
                cv2.circle(
                    frame,
                    index_px,
                    8,
                    (255, 0, 255),
                    -1
                )

                cv2.putText(
                    frame,
                    label,
                    (palm_px[0] - 20, palm_px[1] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

        return frame

    # =========================================

    def has_left(self):
        return self.left_hand is not None

    def has_right(self):
        return self.right_hand is not None

    # =========================================

    def get_left_palm(self):
        return self.left_palm

    def get_right_palm(self):
        return self.right_palm

    def get_left_palm_px(self):
        return self.left_palm_px

    def get_right_palm_px(self):
        return self.right_palm_px

    # =========================================

    def release(self):

        self.cap.release()