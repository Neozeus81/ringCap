import subprocess
import sys

command = ["sudo", "tshark", "-i", "wlan0", "-a", "duration:10","-T", "json"]
res = subprocess.run(command, capture_output=True, text=True)

with open('output.json', 'w') as f:
    f.write(res.stdout)    

