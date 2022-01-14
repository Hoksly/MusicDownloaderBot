import subprocess
from time import sleep
delay = 10 # seconds, increasing after each error

while True:
    subprocess.run('python3.8 main.py', shell=True, check=True)
    sleep(10)
    delay += 10

