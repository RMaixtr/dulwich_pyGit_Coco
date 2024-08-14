import os

os.system('chmod -R 777 /home')
os.system('rsync -r --checksum /home/backup/ /root')
os.system("ps | grep main.py | grep -v grep | awk '{print $1}' | xargs kill")