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

    if cv2.waitKey(1) & 0xFF == ord("q"):
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