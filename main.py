import cv2
import mediapipe as mp
import time
from pynput.keyboard import Controller, Key
import numpy as np

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
keyboard = Controller()

# Variables
prev_x, prev_y = 0, 0
last_gesture_time = 0
debounce_time = 0.35  # Reduced debounce for faster reaction
smooth_factor = 0.5   # Between 0 (no smooth) and 1 (very smooth)
movement_threshold = 25  # Lower threshold for sensitivity

cap = cv2.VideoCapture(0)

def get_center(landmarks):
    x_vals = [lm.x for lm in landmarks]
    y_vals = [lm.y for lm in landmarks]
    return np.mean(x_vals), np.mean(y_vals)

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, _ = img.shape
    current_time = time.time()

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            landmarks = handLms.landmark
            cx, cy = get_center(landmarks)
            cx *= w
            cy *= h

            # Smooth position using interpolation
            smooth_x = int(prev_x * smooth_factor + cx * (1 - smooth_factor))
            smooth_y = int(prev_y * smooth_factor + cy * (1 - smooth_factor))

            dx = smooth_x - prev_x
            dy = smooth_y - prev_y

            if abs(dx) > movement_threshold or abs(dy) > movement_threshold:
                if current_time - last_gesture_time > debounce_time:
                    if abs(dx) > abs(dy):
                        if dx > 0:
                            gesture = "RIGHT"
                            keyboard.press(Key.right)
                            keyboard.release(Key.right)
                        else:
                            gesture = "LEFT"
                            keyboard.press(Key.left)
                            keyboard.release(Key.left)
                    else:
                        if dy < 0:
                            gesture = "UP"
                            keyboard.press(Key.up)
                            keyboard.release(Key.up)
                        else:
                            gesture = "DOWN"
                            keyboard.press(Key.down)
                            keyboard.release(Key.down)

                    last_gesture_time = current_time

            prev_x, prev_y = smooth_x, smooth_y
            cv2.putText(img, f"Gesture Mode Active", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Smooth Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
