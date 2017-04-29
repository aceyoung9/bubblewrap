# Hack. :)
import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")

# Standard imports
import cv2;
# import numpy as np;

# In case you need to check your python version
# print cv2.__version__;

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    edges = cv2.Canny(img, 0, 500)
    cv2.imshow("input", edges)

    key = cv2.waitKey(10)
    if key == 27:
        break

cv2.destroyAllWindows()
cv2.VideoCapture(0).release()
