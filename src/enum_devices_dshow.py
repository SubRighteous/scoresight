import sys
import cv2
from os import path


def enumerate_video_devices_dshow(max_devices=10) -> list[tuple[int, str]]:
    sys.path.append(path.abspath(path.dirname(__file__)))
    
    """Return a list of tuples: (index, name, index, CameraType.OPENCV)."""
    from camera_info import CameraInfo
    devices = []
    for idx in range(max_devices):
        cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
        if cap.isOpened():
            camera_name = f"Camera {idx}"
            devices.append((idx, camera_name, idx, CameraInfo.CameraType.OPENCV))
            cap.release()

    return devices
