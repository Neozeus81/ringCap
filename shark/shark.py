import subprocess

res = subprocess.run(["tshark", "-i wlan0", "-b duration:20", "-w output.pcap"], capture_output=True, text=True)

print(res.stdout)

