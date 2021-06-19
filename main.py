from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import time
import cv2
import os

ap:any = argparse.ArgumentParser()
ap.add_argument(
        "-ip", "--image", type=str,
	help="path to input work_image"
    )
ap.add_argument(
        "-EAST", "--EAST", type=str,
	help="path to input EAST text detector"
    )
ap.add_argument(
        "-c", "--min-confidence", type=float, default=0.5,
	help="minimum probability required to inspect a region(defalut=0.5)"
    )
ap.add_argument(
        "-W", "--width", type=int, default=320,
	help="work_image width (multiple of 32, default=320)"
    )
ap.add_argument(
        "-H", "--height", type=int, default=320,
	help="work_image height (multiple of 32, default=320)"
    )
WARNING = """
The EAST text requires that your input work_image dimensions be multiples of 32,
while choosing your width (--width) and height (--height),
make sure they are multiples of 32
"""

args:dict = vars(ap.parse_args())


work_image: np.array = cv2.imread(os.path.abspath(args["image"]))
orig: np.array = work_image.copy()

print(orig)

IMG_H: int = work_image.shape[0]
IMG_W: int = work_image.shape[1]


newW: int = args["width"]
newH: int = args["height"]

if (newW + newH)%32 != 0:
    print("please read instructions")
    exit(1)

rW = IMG_W / int(newW)
rH = IMG_H / int(newH)
work_image = cv2.resize(work_image, (newW, newH))
(H, W) = work_image.shape[:2]

# define the two output layer names for the EAST detector model that
# we are interested -- the first is the output probabilities and the
# second can be used to derive the bounding box coordinates of text

layer_names = [
	"feature_fusion/Conv_7/Sigmoid",
	"feature_fusion/concat_3"
    ]
# load the pre-trained EAST text detector
print("[INFO] loading EAST text detector...")
net = cv2.dnn.readNet(args["EAST"])

# construct a blob from the image and then perform a forward pass of
# the model to obtain the two output layer sets

blob = cv2.dnn.blobFromImage(
        work_image,
        1.0, 
        (W, H),
        (123.68, 116.78, 103.94), 
        swapRB=True, crop=False
    )

start = time.time()
net.setInput(blob)
(scores, geometry) = net.forward(layerNames)
end = time.time()
# show timing information on text prediction
print("[INFO] text detection took {:.6f} seconds".format(end - start))
