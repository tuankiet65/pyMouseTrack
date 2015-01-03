#!/usr/bin/python3

from PIL import Image, ImageDraw


class AntiAliasingPillow():

    def __init__(self, size, mode, color=0):
        self.SSAA_RATIO = 2
        self.size = size
        self.image = Image.new(
            mode, (self.size[0] * self.SSAA_RATIO, self.size[1] * self.SSAA_RATIO), color)
        self.draw = ImageDraw.Draw(self.image)

    def line(self, p1, p2, width=0, fill=None):
        self.draw.line([(p1[0] * self.SSAA_RATIO, p1[1] * self.SSAA_RATIO),
                        (p2[0] * self.SSAA_RATIO, p2[1] * self.SSAA_RATIO)], width=0, fill=fill)

    def circle(self, p, radius, fill=None, outline=None):
        self.draw.ellipse([((p[0] - radius) * self.SSAA_RATIO, (p[1] - radius) * self.SSAA_RATIO),
                           ((p[0] + radius) * self.SSAA_RATIO, (p[1] + radius) * self.SSAA_RATIO)], fill=fill, outline=outline)

    def original_size(self):
        return self.image.resize(
            self.size, resample=Image.ANTIALIAS)
