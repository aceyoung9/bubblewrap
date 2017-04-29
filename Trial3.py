# Hack. :)
import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")

# Standard imports
import cv2;
# import numpy as np;

# In case you need to check your python version
# print cv2.__version__;

# Read image
im = cv2.imread("test-images/fuzzy_blurry_bubble.jpg", 0)

edges = cv2.Canny(im, 0, 500)

# Show keypoints
cv2.imshow("Edges", edges)
cv2.waitKey(0)
