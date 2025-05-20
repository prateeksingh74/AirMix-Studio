import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=2):
        self.hands = mp.solutions.hands.Hands(max_num_hands=max_hands, min_detection_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
        return frame, results

