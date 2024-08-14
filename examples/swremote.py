localrep = "/home/backup"
remote_url = "https://gitee.com/ForeverXJie/test.git"

import git

git.rw()

git.swRemote(localrep, remote_url)

git.ro()
