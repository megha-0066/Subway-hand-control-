# Subway Hand Control

A gesture-controlled version of the popular Subway Surfer game using **computer vision** and **hand tracking**. This project allows players to control the game using **hand movements**, providing an interactive and touch-free gaming experience.

---

## Project Overview

The **Subway Hand Control** project uses **MediaPipe** for real-time hand tracking and **OpenCV** for capturing video from a webcam. Hand gestures are translated into keyboard inputs to control the game, such as moving left, right, jumping, and sliding. This provides a smooth, immersive, and fun way to play the Subway Surfer game without using a keyboard.

---

## How It Works

1. **Webcam captures hand movements** in real-time.
2. **MediaPipe detects hand landmarks** to track finger and palm positions.
3. **Gesture recognition logic** interprets specific hand movements:
   - Swipe Left → Move character left
   - Swipe Right → Move character right
   - Raise Hand → Jump
   - Lower Hand → Slide
4. **Pynput simulates keyboard presses** to control the game based on recognized gestures.
5. The game responds in real-time to gestures, creating an interactive experience.

---

## Features

- Real-time hand gesture detection.
- Smooth and responsive game controls.
- No-touch gameplay — control the game entirely with your hand.
- Easy to integrate with any running instance of Subway Surfer or similar games.

---

## Folder Structure
Subway-hand-control/
│
├─ main.py # Main script to run gesture control
├─ gesture_control.py # Gesture detection and keyboard mapping
├─ utils.py # Helper functions (if any)
├─ requirements.txt # Project dependencies
├─ README.md



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/megha-0066/Subway-hand-control-.git
   cd Subway-hand-control-
