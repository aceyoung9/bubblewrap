# Hack. :)
import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")

# Standard imports
import cv2;
import numpy as np;

# In case you need to check your python version
# print cv2.__version__;

cap = cv2.VideoCapture(0)
list_of_circles = []

while True:
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    img = cv2.Canny(img, 0, 500)

    # img = cv2.GaussianBlur(img, (15, 15), 20)

    circles = cv2.HoughCircles(img,
                               cv2.HOUGH_GRADIENT,
                               1,
                               img[0].size / 5,
                               param1=50, param2=50, minRadius=100, maxRadius=img.shape[1] / 3)

    if circles is None:
        circles = np.uint16(np.around(np.zeros((1, 4, 3))))
    else:
        circles = np.uint16(np.around(circles))



    for i in circles[0, :]:

        potential_circle = i[0:1]
        if potential_circle != [0]:
            list_of_circles.append(potential_circle)

        # print(i[0:2])
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow("input", cimg)

    key = cv2.waitKey(10)
    if key == 27:
        break

cv2.destroyAllWindows()
cv2.VideoCapture(0).release()

f1 = open('./circles.txt', 'w+')
# f1.writelines(list_of_circles)
for circle in list_of_circles:
    f1.write(str(circle))
    f1.write('\n')


