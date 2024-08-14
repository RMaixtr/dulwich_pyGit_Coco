localrep = "/home/backup"
otaPath = "/root/preset/app/ota.py"

from maix import camera, display, image  # 引入python模块包

image.load_freetype("/root/preset/fonts/simhei.ttf")
hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
hello_img.draw_string(10, 115, 'Pull', scale=1.0, color=(255, 255, 255), thickness=1)
display.show(hello_img)

import git, time

if not git.isOnline(localrep):
    hello_img = image.new(size=(320, 240), color=(0, 0, 0), mode="RGB")
    hello_img.draw_string(10, 115, 'Network connection error', scale=1.0, color=(255, 255, 255), thickness=1)
    display.show(hello_img)
    time.sleep(2)
    exit()

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

with open(otaPath) as f:
    code = f.read()
exec(code)

git.ro()
