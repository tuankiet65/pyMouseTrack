#!/usr/bin/python3

from pymouse import PyMouse, PyMouseEvent
import time


class MouseEvent(PyMouseEvent):

    def __init__(self, image):
        PyMouseEvent.__init__(self)
        self.prev = PyMouse().position()
        self.lastStop = time.time()
        self.BLACK = (0, 0, 0, 255)
        self.image = image

    def move(self, x, y):
        curr = (x, y)
        self.image.line(self.prev, curr, width=0, fill=self.BLACK)
        secondsEplased = int(time.time() - self.lastStop)
        if secondsEplased > 2:
            self.lastStop = time.time()
            radiusOuter = (secondsEplased % 60) * 5
            radiusInner = (secondsEplased // 60) * 10 + 5
            self.image.circle(self.prev, radiusOuter, outline=self.BLACK)
            self.image.circle(
                self.prev, radiusInner, outline=self.BLACK, fill=self.BLACK)
        self.prev = curr
