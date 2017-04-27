# Hack. :)
import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")

# Standard imports
import cv2;
import numpy as np;

# print cv2.__version__;

# Read image
im = cv2.imread("test-images/still2.jpg", cv2.IMREAD_GRAYSCALE)
im = cv2.bitwise_not(im)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

params.maxThreshold = 200
params.minThreshold = 0

params.filterByArea = True
params.minArea = 150

params.filterByInertia = False
# params.minInertiaRatio = 0.5
#
params.filterByColor = False
params.minRepeatability = 0
params.filterByCircularity = False
# params.minCircularity = 0.85

# Set up the detector
detector = cv2.SimpleBlobDetector(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(cv2.bitwise_not(im), keypoints, np.array([]), (255, 180, 0),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
