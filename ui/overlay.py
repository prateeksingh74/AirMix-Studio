import cv2

def draw_ui(frame):
    h, w, _ = frame.shape

    # Volume Bar
    cv2.rectangle(frame, (50, 100), (80, 400), (255, 255, 255), 2)
    cv2.putText(frame, "Volume", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    # Speed Bar
    cv2.rectangle(frame, (w - 80, 100), (w - 50, 400), (255, 255, 255), 2)
    cv2.putText(frame, "Speed", (w - 100, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    # FX Zone
    cv2.rectangle(frame, (w//2 - 50, 430), (w//2 + 50, 480), (0, 255, 255), 2)
    cv2.putText(frame, "FX Trigger", (w//2 - 60, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 2)

    return frame

