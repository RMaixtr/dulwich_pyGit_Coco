import git
import os
from io import RawIOBase

localrep = "/home"


class NewStream(RawIOBase):
    """Fallback if stdout or stderr are unavailable, does nothing."""

    def read(self, size=-1):
        return None

    def readall(self):
        return None

    def readinto(self, b):
        return None

    def write(self, b):
        print(b)
        return None


git.rw()
steam = NewStream()
if os.path.exists(localrep + "/cclb_launch"):
    os.remove(localrep + "/cclb_launch")
if git.activeBranch(localrep) != b'master':
    git.checkout(localrep, 'master', steam)
else:
    git.checkout(localrep, 'en', steam)
if os.path.exists("/root/CocoPi.py"):
    os.remove("/root/CocoPi.py")
os.system('chmod -R 777 /home')
os.system('reboot')
git.ro()
