import sys
import cv2
from os import path
from pygrabber.dshow_graph import FilterGraph

def enumerate_video_devices_dshow(max_devices=10) -> list[tuple[int, str]]:
    sys.path.append(path.abspath(path.dirname(__file__)))
    
    """Return a list of tuples: (index, name, index, CameraType.OPENCV)."""
    from camera_info import CameraInfo
    devices = []
    
    graph = FilterGraph()
    devices_list = graph.get_input_devices()

    if not devices_list:
        print("No camera devices found.")
        return devices

    print("Available camera devices:")
    
    for index, name in enumerate(devices_list):
        print(f"Index {index}: {name}")
        devices.append((index, name, index, CameraInfo.CameraType.OPENCV))
        
    #for idx in range(max_devices):
        
        # print(f"Getting Video Capture on {idx}")
        
        # cap = cv2.VideoCapture(idx, cv2.CAP_MSMF)
        # if not cap.isOpened():
        #     cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
        
        # if cap.isOpened():
        #     try:
        #         if hasattr(cap, 'getBackendName'):
        #             backend_name = cap.getBackendName()
        #             print(f"Found device {idx} with backend: {backend_name}")
                    
        #             camera_name = f"Camera {idx}"
        #         devices.append((idx, camera_name, idx, CameraInfo.CameraType.OPENCV))
                
        #     finally:
        #         cap.release()
        # else: 
        #     break

    return devices
