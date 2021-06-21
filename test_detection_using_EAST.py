from imutils.object_detection import non_max_suppression
import numpy as np
import time
import cv2
import os



image_path = "https://i2.wp.com/syncedreview.com/wp-content/uploads/2020/04/image-82.png"
model_path = os.path.abspath("./frozen_east_text_detection.pb")
min_confidence = 0.5

WARNING = """
The EAST text requires that your input work_image dimensions be multiples of 32,
while choosing your width (--width) and height (--height),
make sure they are multiples of 32
"""

work_image: np.array = cv2.imread(image_path)
orig: np.array = work_image.copy()

IMG_H: int = work_image.shape[0]
IMG_W: int = work_image.shape[1]


# define the two output layer names for the EAST detector model that
# we are interested -- the first is the output probabilities and the
# second can be used to derive the bounding box coordinates of text

layer_names = [
	"feature_fusion/Conv_7/Sigmoid",
	"feature_fusion/concat_3"
]

net = cv2.dnn.readNet(model_path)

# construct a blob from the image and then perform a forward pass of
# the model to obtain the two output layer sets

scale_factor: float = 1.0
size: tuple(int, int) = (IMG_W, IMG_H)
scaler_mean: tuple(float, float, float) = (123.68, 116.78, 103.94)

blob = cv2.dnn.blobFromImage(
        work_image,
        scale_factor, 
        size,
        scaler_mean, 
        swapRB=True, 
        crop=False
)

start = time.time()
net.setInput(blob)
(scores, geometry) = net.forward(layer_names)
end = time.time()
# show timing information on text prediction
print("[INFO] text detection took {:.6f} seconds".format(end - start))
