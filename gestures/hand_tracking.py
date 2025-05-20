import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=2):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.6
        )
        self.drawer = mp.solutions.drawing_utils
        self.hand_connections = mp.solutions.hands.HAND_CONNECTIONS

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.drawer.draw_landmarks(frame, hand_landmarks, self.hand_connections)
        return frame, result

