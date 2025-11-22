import subprocess
import sys

class Shark:

    def __init__(self, duration, interface, filename):
        self.duration = duration
        self.interface = interface
        self.filename = filename
    
    def sniff(self):

        command = ["sudo", "tshark", "-i", self.interface, "-c", str(self.duration),"-T", "json"]
        res = subprocess.run(command, capture_output=True, text=True)

        with open(self.filename, 'w') as f:
            f.write(res.stdout)


