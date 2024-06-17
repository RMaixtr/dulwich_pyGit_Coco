import os
import sys
from io import RawIOBase
from dulwich import porcelain
from dulwich.client import get_transport_and_path
from dulwich.porcelain import get_remote_repo
from dulwich.repo import Repo
from dulwich.walk import Walker


def ro():
    os.system("/etc/init.d/S01mount_ro start")


def rw():
    os.system("/etc/init.d/S01mount_ro stop")


class NoneStream(RawIOBase):
    """Fallback if stdout or stderr are unavailable, does nothing."""

    def read(self, size=-1):
        return None

    def readall(self):
        return None

    def readinto(self, b):
        return None

    def write(self, b):
        return None


def log(localRep):
    repo = Repo(localRep)
    walker = Walker(repo, sorted(repo.get_refs().values(), reverse=True))
    for entry in walker:
        commit = entry.commit
        print(f"commit {commit.id.decode()}")
        print(f"Author: {commit.author.decode()} <{commit.author.decode()}>")
        print(f"Date: {commit.author_time}")
        print()
        print(f"    {commit.message.decode()}")
        print()


def showChanges(localRep, outStream=sys.stdout):
    porcelain.show(localRep, outstream=outStream)


def activeBranch(localRep):
    return porcelain.active_branch(localRep)


def checkout(localRep, branch, progStream=None):
    r = Repo(localRep)
    if progStream is None:
        progStream = NoneStream()
    try:
        porcelain.checkout_branch(r, 'origin/' + branch, outstream=progStream)
    except porcelain.CheckoutError as e:
        print("CheckoutError:", e)
        porcelain.reset(r, 'hard')
        porcelain.checkout_branch(r, 'origin/' + branch, outstream=progStream)


def pull(repo_path, progStream=None):
    if progStream is None:
        progStream = NoneStream()
    porcelain.pull(repo_path, refspecs=porcelain.active_branch(repo_path), outstream=progStream)


def isOnline(localRep):
    r = Repo(localRep)
    (remote_name, remote_location) = get_remote_repo(r, None)
    client, path = get_transport_and_path(
        remote_location, config=r.get_config_stack()
    )
    try:
        client.fetch(path, r)
        return True
    except Exception:
        return False

