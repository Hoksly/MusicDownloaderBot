import subprocess
from time import sleep
delay = 60

while True:
    subprocess.run('venv/bin/python3.8 main.py', shell=True, check=True)
    sleep(delay)


