#!/usr/bin/python3

from pymouse import PyMouse
from PIL import Image, ImageDraw
import time
import pyscreenshot

class AntiAliasing():
	def __init__(self, size):
		self.AA_RATIO=3
		self.size_x=size[0]
		self.size_y=size[1]
		self.image=Image.new("RGBA", (self.size_x*self.AA_RATIO, self.size_y*self.AA_RATIO), color=(255, 255, 255, 0))
		self.draw=ImageDraw.Draw(self.image)

	def line(self, p1, p2, width=0, fill=None):
		self.draw.line([(p1[0]*self.AA_RATIO, p1[1]*self.AA_RATIO), (p2[0]*self.AA_RATIO, p2[1]*self.AA_RATIO)], width=0, fill=fill)

	def circle(self, p, radius, fill=None, outline=None):
		self.draw.ellipse([((p[0]-radius)*self.AA_RATIO, (p[1]-radius)*self.AA_RATIO), ((p[0]+radius)*self.AA_RATIO, (p[1]+radius)*self.AA_RATIO)], fill=fill, outline=outline)

	def save(self, filename):
		result=self.image.resize((self.size_x, self.size_y), resample=Image.ANTIALIAS)
		screen=Image.blend(pyscreenshot.grab(), Image.new("RGB", (self.size_x, self.size_y), color=(255, 255, 255)), alpha=0.2)
		#self.image.resize((self.size_x, self.size_y), resample=Image.ANTIALIAS).save(filename)
		screen.paste(result, mask=result)
		screen.save(filename)


m=PyMouse()
image=AntiAliasing(m.screen_size())
prev=m.position()
lastStop=time.time()

try:
	while True:
		curr=m.position()
		if curr!=prev:
			image.line(prev, curr, width=0, fill=(0, 0, 0, 255))
			secondsEplased=int(time.time()-lastStop)
			if secondsEplased>4:
				lastStop=time.time()
				radiusOuter=(secondsEplased%60)*5
				radiusInner=(secondsEplased//60)*10+5
				image.circle(prev, radiusOuter, outline=(0, 0, 0, 255))
				image.circle(prev, radiusInner, outline=(0, 0, 0, 255), fill=(0, 0, 0, 255))
			prev=curr
except KeyboardInterrupt as e:
	image.save("test.png")