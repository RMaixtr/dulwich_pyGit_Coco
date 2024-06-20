localrep = "/home"

from maix import camera, display, image  # 引入python模块包

image.load_freetype("/root/preset/fonts/simhei.ttf")
hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
hello_img.draw_string(10, 115, 'Pull', scale=1.0, color=(255, 255, 255), thickness=1)
display.show(hello_img)

import os, git, time

if not git.isOnline(localrep):
    hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
    hello_img.draw_string(10, 115, 'Network connection error', scale=1.0, color=(255, 255, 255), thickness=1)
    display.show(hello_img)
    time.sleep(2)
    exit()
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

git.pull(localrep, steam)
hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
commit, Author, Date, message = git.__log__(localrep)
hello_img.draw_string(10, 50, commit, scale=1.0, color=(255, 255, 255), thickness=1)
hello_img.draw_string(10, 100, Author, scale=1.0, color=(255, 255, 255), thickness=1)
hello_img.draw_string(10, 150, Date, scale=1.0, color=(255, 255, 255), thickness=1)
hello_img.draw_string(10, 200, message, scale=1.0, color=(255, 255, 255), thickness=1)
display.show(hello_img)

os.system('chmod -R 777 /home')
os.system('rsync -r --checksum /home/backup/ /root')
os.system("ps | grep main.py | grep -v grep | awk '{print $1}' | xargs kill")
git.ro()
