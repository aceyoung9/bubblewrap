import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")

import cv2
import unittest

class TestUSBWebcamDidMount(unittest.TestCase):
    def setUp(self):
        self.cap0 = cv2.VideoCapture(0)
        self.cap0.set(3,160)
        self.cap0.set(4,120)
        self.cap1 = cv2.VideoCapture(1)
        self.cap1.set(3,160)
        self.cap1.set(4,120)

    def test_mount(self):
        ret0, frame0 = self.cap0.read()
        self.assertTrue(ret0, 'Cam 1 ain\'t mounting.')

        ret1, frame1 = self.cap1.read()
        self.assertTrue(ret1, 'Cam 1 ain\'t mounting.')
