import cv2
from gestures.hand_tracking import HandTracker
from ui.overlay import draw_ui

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # mirror effect
        frame, _ = tracker.find_hands(frame)
        frame = draw_ui(frame)

        cv2.imshow("AirMix Studio", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

