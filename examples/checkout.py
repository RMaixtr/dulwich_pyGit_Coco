localrep = "/home"

from maix import camera, display, image

image.load_freetype("/root/preset/fonts/simhei.ttf")
hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
hello_img.draw_string(10, 115, 'Checkout', scale=1.0, color=(255, 255, 255), thickness=1)
display.show(hello_img)

import os, git

if os.path.exists(localrep + "/cclb_launch"):
    os.remove(localrep + "/cclb_launch")

from io import RawIOBase


class NewStream(RawIOBase):
    def write(self, b):
        hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
        hello_img.draw_string(10, 115, str(b), scale=1.0, color=(255, 255, 255), thickness=1)
        display.show(hello_img)
        return None


git.rw()
steam = NewStream()
if os.path.exists(localrep + "/cclb_launch"):
    os.remove(localrep + "/cclb_launch")
if git.activeBranch(localrep) != b'master':
    git.checkout(localrep, 'master', steam)
else:
    git.checkout(localrep, 'en', steam)
hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
hello_img.draw_string(10, 115, 'Reconstruct directory', scale=1.0, color=(255, 255, 255), thickness=1)
display.show(hello_img)
os.system('chmod -R 777 /home')
os.system('rsync -r --checksum /home/backup/ /root')
os.system("ps | grep main.py | grep -v grep | awk '{print $1}' | xargs kill")
git.ro()
