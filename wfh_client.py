import subprocess
import os
import time


ROBOT_IP = "192.168.1.177"
ROBOT_PORT = "50000"
CLIENT_PORT = "50001"
DEVICE_ID = "1"


# Initially, mute auto coming from client.
os.system("touch .audio.bot.pause")

# Stream audio to robot.
subprocess.Popen(["python3", "audio_stream_server.py", "44100", CLIENT_PORT])

# Give time for remote server to be started.
time.sleep(5)

# Receive audio from robot.
subprocess.Popen(["python3", "audio_stream_client.py", ROBOT_IP, ROBOT_PORT, DEVICE_ID, "16000"])

while(True):
    pass
