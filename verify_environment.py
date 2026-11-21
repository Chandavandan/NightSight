
import torch
import torchvision
import cv2
import numpy as np
import pandas as pd
import matplotlib
import sklearn
import ultralytics
import scipy
import yaml

print("=" * 45)
print("       NIGHT SIGHT ENVIRONMENT CHECK")
print("=" * 45)

print("PyTorch:", torch.__version__)
print("Torchvision:", torchvision.__version__)
print("CUDA:", torch.version.cuda)
print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print(
        "GPU Memory:",
        round(
            torch.cuda.get_device_properties(0).total_memory
            / 1024**3, 2
        ), "GB"
    )

print("OpenCV:", cv2.__version__)
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Matplotlib:", matplotlib.__version__)
print("Scikit-learn:", sklearn.__version__)
print("Ultralytics:", ultralytics.__version__)
print("SciPy:", scipy.__version__)

print("=" * 45)
print("ENVIRONMENT VERIFICATION COMPLETE")
print("=" * 45)
