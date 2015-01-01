# pyMousePath

## What is this:
A clone of [IOGraphica](http://iographica.com/) written in Python

## Dependencies:
* [PyUserInput](https://github.com/SavinaRoja/PyUserInput) for reading mouse input.
* [Pillow](https://github.com/python-pillow/Pillow) for creating images.
* [pyscreenshot](https://github.com/ponty/pyscreenshot) for capturing screenshots.
* If you are running an OS other than Windows, you will have to install one of these packages (using your OS's package manager, not pip):
  * scrot (recommended)
  * ImageMagick
  * PyGTK2
  * PyQT4

## To do
* Colorful Scheme.
* Faster (Pillow and pyscreenshot and anti-aliasing are the bottleneck)

## Done
* Use event callback instead of polling mouse position continuously.

## License
Haven't decided yet.