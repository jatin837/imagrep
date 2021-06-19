from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument(
        "-ip", "--image-path", type=str,
	help="path to input image"
    )
ap.add_argument(
        "-EAST", "--EAST", type=str,
	help="path to input EAST text detector"
    )
ap.add_argument(
        "-c", "--min-confidence", type=float, default=0.5,
	help="minimum probability required to inspect a region"
    )
ap.add_argument(
        "-w", "--width", type=int, default=320,
	help="image width (multiple of 32, default=320)"
    )
ap.add_argument(
        "-h", "--height", type=int, default=320,
	help="image height (multiple of 32, default=320)"
    )
args = vars(ap.parse_args())
