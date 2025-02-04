import os
import sys
import time
import cv2
from cvzone.PlotModule import LivePlot
import numpy as np

# setting path
sys.path.append("../")

tapo_username = os.getenv("TAPO_USERNAME")
tapo_password = os.getenv("TAPO_PASSWORD")
tapo_local_ip = os.getenv("TAPO_LOCAL_IP")
rtsp_port = 554

RTSP_URL = f"rtsp://{tapo_username}:{tapo_password}@{tapo_local_ip}:{rtsp_port}/stream1"
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

# cap = cv2.VideoCapture(r"YourVideoPath")
cap = cv2.VideoCapture(RTSP_URL)

# Initializing the Plot
xPlot = LivePlot(w=640, yLimit=[0, 500], interval=0.01)

# Previous Time (used to calculate FPS)
pTime = 0

while True:
    success, img = cap.read()

    img = cv2.resize(img, (640, 480))

    if not success:
        break

    # Calculating the fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Updating the plot
    imgPlot = xPlot.update(fps)

    # Concatenating input image and the plot
    result_img = np.hstack([img, imgPlot])

    cv2.imshow("Image and Plot", result_img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
