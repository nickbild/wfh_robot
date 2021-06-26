import subprocess
import os


ROBOT_IP = "192.168.1.177"
PORT = 4445


# Initially, mute auto coming from client.
os.system("touch .audio.bot.pause")

# Stream audio to robot.
subprocess.Popen(["python3", "audio_stream_server.py"], 44100)

# Receive audio from robot.
subprocess.Popen(["python3", "audio_stream_client.py"], ROBOT_IP, PORT, 16000)

while(True):
    pass
