#!/usr/bin/python3

from pymouse import PyMouse, PyMouseEvent
from PIL import Image, ImageDraw
import time
import pyscreenshot


class AntiAliasing():

    def __init__(self, size):
        self.size = size
        self.image = Image.new(
            "RGBA", (self.size[0] * SSAA_RATIO, self.size[1] * SSAA_RATIO), color=(255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)

    def line(self, p1, p2, width=0, fill=None):
        self.draw.line([(p1[0] * SSAA_RATIO, p1[1] * SSAA_RATIO),
                        (p2[0] * SSAA_RATIO, p2[1] * SSAA_RATIO)], width=0, fill=fill)

    def circle(self, p, radius, fill=None, outline=None):
        self.draw.ellipse([((p[0] - radius) * SSAA_RATIO, (p[1] - radius) * SSAA_RATIO),
                           ((p[0] + radius) * SSAA_RATIO, (p[1] + radius) * SSAA_RATIO)], fill=fill, outline=outline)

    def save(self, filename):
        result = self.image.resize(
            self.size, resample=Image.ANTIALIAS)
        screen = Image.blend(pyscreenshot.grab(), Image.new(
            "RGB", self.size, color=(255, 255, 255)), alpha=0.2)
        screen.paste(result, mask=result)
        screen.save(filename)


class MouseEvent(PyMouseEvent):

    def __init__(self):
        PyMouseEvent.__init__(self)
        self.prev = PyMouse().position()
        self.lastStop = time.time()

    def move(self, x, y):
        curr = (x, y)
        image.line(self.prev, curr, width=0, fill=BLACK)
        secondsEplased = int(time.time() - self.lastStop)
        if secondsEplased > 4:
            self.lastStop = time.time()
            radiusOuter = (secondsEplased % 60) * 5
            radiusInner = (secondsEplased // 60) * 10 + 5
            image.circle(self.prev, radiusOuter, outline=BLACK)
            image.circle(self.prev, radiusInner, outline=BLACK, fill=BLACK)
        self.prev = curr

SSAA_RATIO = 2
image = AntiAliasing(PyMouse().screen_size())
lastStop = time.time()
BLACK = (0, 0, 0, 255)

mouseTrack = MouseEvent()
mouseTrack.run()
image.save("test.png")