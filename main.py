"""
=========================================
OpenHands
main.py

Main Application

Author : Veer Pratap
=========================================
"""

import cv2

from tracker import HandTracker
from mouse import MouseController
from movement import MovementController
from gestures import GestureController
from controller import GameController
from calibration import Calibration
from ui import UI
from utils import FPSCounter, print_header


def main():

    print_header()

    print("Initializing OpenHands...\n")

    # ----------------------------------
    # Initialize Modules
    # ----------------------------------

    print("[1/8] Tracker...")
    tracker = HandTracker()

    print("[2/8] Mouse...")
    mouse = MouseController()

    print("[3/8] Movement...")
    movement = MovementController()

    print("[4/8] Calibration...")
    calibration = Calibration()

    print("[5/8] Gestures...")
    gestures = GestureController()

    print("[6/8] Controller...")
    controller = GameController()

    print("[7/8] UI...")
    ui = UI()

    print("[8/8] FPS...")
    fps_counter = FPSCounter()

    print("\n===================================")
    print("OpenHands Started Successfully!")
    print("===================================")
    print("C  -> Calibrate")
    print("R  -> Reset Calibration")
    print("Q  -> Quit")
    print("===================================\n")

    # ==================================
    # Main Loop
    # ==================================

    while True:

        # -----------------------------
        # Get Camera Frame
        # -----------------------------

        frame = tracker.update()

        if frame is None:
            continue

        # -----------------------------
        # Detect Gestures
        # -----------------------------

        gesture = gestures.update(tracker.right_hand)

        # -----------------------------
        # Mouse Control
        # -----------------------------

        if calibration.is_calibrated():
            mouse.update(tracker.right_hand)

        # -----------------------------
        # Movement Control
        # -----------------------------

        if calibration.is_calibrated():
            movement.update(tracker, calibration)
        else:
            movement.current_direction = "IDLE"

        # -----------------------------
        # Game Controller
        # -----------------------------

        direction = movement.get_direction()

        controller.update(
            gesture,
            direction
        )

        # -----------------------------
        # FPS
        # -----------------------------

        fps = fps_counter.update()

        # -----------------------------
        # Draw UI
        # -----------------------------

        frame = ui.draw(
            frame=frame,
            tracker=tracker,
            gesture=gesture,
            mouse=mouse,
            movement=movement,
            fps=fps
        )

        # -----------------------------
        # Calibration Status
        # -----------------------------

        if calibration.is_calibrated():

            cv2.putText(
                frame,
                "STATUS : CALIBRATED",
                (20, frame.shape[0] - 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        else:

            cv2.putText(
                frame,
                "STATUS : PRESS C TO CALIBRATE",
                (20, frame.shape[0] - 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

        # -----------------------------
        # Show Window
        # -----------------------------

        cv2.imshow("OpenHands", frame)

        # -----------------------------
        # Keyboard
        # -----------------------------

        key = cv2.waitKey(1) & 0xFF

        if key == ord("c"):

            if calibration.calibrate(tracker):
                print("\nCalibration Successful!\n")
            else:
                print("\nShow BOTH hands and press C.\n")

        elif key == ord("r"):

            calibration.reset()
            print("\nCalibration Reset.\n")

        elif key == ord("q") or key == 27:

            break

    # ==================================
    # Cleanup
    # ==================================

    tracker.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
