#!/usr/bin/python3

from .AntiAliasingPillow import AntiAliasingPillow
from .MouseEvent import MouseEvent
from pymouse import PyMouse
from PIL import ImageEnhance
import pyscreenshot
import tempfile
import pyimgur
import os
import sys


def UploadToImgurFromPIL(image, format, imgur, title=None, description=None, album=None):
    temp = tempfile.mkstemp()
    image.save(temp[1], format=format)
    image_object = imgur.upload_image(
        temp[1], title=title, description=description, album=album)
    os.remove(temp[1])
    return image_object


def MousePathAndScreenshotOverlay(mousePath, screenshot):
    BRIGHTNESS = 0.5
    screen = ImageEnhance.Brightness(screenshot).enhance(BRIGHTNESS)
    screen.paste(mousePath, mask=mousePath)
    return screen


def main():
    if len(sys.argv) < 2:
        print("Usage: pyMouseTrack <filename>")
        sys.exit()
    filename = sys.argv[1]
    image = AntiAliasingPillow(
        PyMouse().screen_size(), "RGBA", (255, 255, 255, 0))
    mouse = MouseEvent(image)
    mouse.start()
    try:
        mouse.join()
    except KeyboardInterrupt as e:
        MousePathAndScreenshotOverlay(
            image.original_size(), pyscreenshot.grab()).save(filename)

if __name__ == '__main__':
    main()
