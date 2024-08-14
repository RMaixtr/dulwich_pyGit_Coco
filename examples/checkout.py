localrep = "/home/backup"
otaPath = "/root/preset/app/ota.py"

from maix import camera, display, image

image.load_freetype("/root/preset/fonts/simhei.ttf")
hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
hello_img.draw_string(10, 115, 'Checkout', scale=1.0, color=(255, 255, 255), thickness=1)
display.show(hello_img)

import git
from io import RawIOBase


class NewStream(RawIOBase):
    def write(self, b):
        hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
        hello_img.draw_string(10, 115, str(b), scale=1.0, color=(255, 255, 255), thickness=1)
        display.show(hello_img)
        return None


git.rw()
steam = NewStream()

if git.activeBranch(localrep) != b'zh':
    git.checkout(localrep, 'zh', steam)
else:
    git.checkout(localrep, 'en', steam)

hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
hello_img.draw_string(10, 115, 'Reconstruct directory', scale=1.0, color=(255, 255, 255), thickness=1)
display.show(hello_img)

with open(otaPath) as f:
    code = f.read()
exec(code)

git.ro()
