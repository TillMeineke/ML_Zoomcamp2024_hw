# Stolen from https://lindevs.com/capture-rtsp-stream-from-ip-camera-using-opencv/

import cv2
import os

RTSP_URL = 'rtsp://tapoDogCam2:12HundeOhr!@192.168.178.43:554/stream1'
# RTSP_URL = 'rtsp://192.168.178.43:554/stream1'


os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

while True:
    _, frame = cap.read()
    cv2.imshow('RTSP stream', frame)

    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# import urllib.parse

# username = "tapoDogCam2"
# password = "12HundenOhr!"
# ip_address = "192.168.178.43"
# port = "554"
# stream_path = "stream1"

# encoded_url = f"rtsp://{urllib.parse.quote(username)}:{urllib.parse.quote(password)}@{ip_address}:{port}/{stream_path}"
# print("Encoded URL:", encoded_url)

import cv2
import os
import time

RTSP_URL = 'rtsp://tapoDogCam2:12HundeOhr!@192.168.178.43:554/stream1'
# RTSP_URL = 'rtsp://192.168.178.43:554/stream1'

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

cv2.namedWindow('RTSP stream', cv2.WINDOW_NORMAL)  # Allow resizing if needed

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to retrieve frame. Exiting...')
            break

        cv2.imshow('RTSP stream', frame)

        # Wait for 'q' or 'Esc' key press to exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 'q' or 'Esc' key
            print('Exiting...')
            break
except KeyboardInterrupt:
    print('Interrupted by user. Exiting...')
finally:
    cap.release()
    # Destroy the specific window and flush events
    cv2.destroyWindow('RTSP stream')
    cv2.waitKey(1)  # Process GUI events to ensure cleanup
    time.sleep(0.5)  # Small delay to allow the window to close
    cv2.destroyAllWindows()
    cv2.waitKey(1)  # Extra flush in case OpenCV lags on macOS
    print('Cleanup complete.')