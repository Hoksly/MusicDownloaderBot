import subprocess
from time import sleep

while True:
    subprocess.run('python3.8 main.py', shell=True, check=True)
    sleep(10)

