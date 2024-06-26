import os
import sys
from io import RawIOBase
from dulwich import porcelain
from dulwich.porcelain import get_remote_repo
from dulwich.repo import Repo
from dulwich.walk import Walker
import requests


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


def __log__(localRep):
    repo = Repo(localRep)
    walker = Walker(repo, sorted(repo.get_refs().values(), reverse=True))
    for entry in walker:
        commit = entry.commit
        return f"commit {commit.id.decode()}", f"Author: {commit.author.decode()} <{commit.author.decode()}>", \
               f"Date: {commit.author_time}", f"    {commit.message.decode()}"


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


def reset(localRep):
    repo = Repo(localRep)
    head_ref = repo.head()
    head_commit = repo[head_ref]
    parent_commit = repo[head_commit.parents[0]]
    porcelain.reset(repo, 'hard', parent_commit.tree)


def recovery(localRep):
    r = Repo(localRep)
    porcelain.reset(r, 'hard')


def clone(source, target=None, depth: int = None):
    porcelain.clone(source, target, depth=depth)


def isOnline(localRep):
    r = Repo(localRep)
    (remote_name, remote_location) = get_remote_repo(r, None)
    try:
        response = requests.get(remote_location)
        if response.status_code == 200:
            # print("Connection successful.")
            return True
        else:
            # print(f"Connection failed with status code: {response.status}")
            return False
    except Exception as e:
        # print(f"Connection failed: {e}")
        return False
