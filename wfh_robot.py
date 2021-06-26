import subprocess
import os


CLIENT_IP = "192.168.1.113"
ROBOT_PORT = "4446"
CLIENT_PORT = "4447"
DEVICE_ID = "2"


# Initially, make sure robot is NOT muted.
os.system("rm -f .audio.bot.pause")

# Start up the camera in the background.
subprocess.Popen(["python3", "image_capture_loop.py"])

# Start simple web server.
subprocess.Popen(["python3", "web_server.py"])

# Stream audio to client.
subprocess.Popen(["python3", "audio_stream_server.py", "16000", ROBOT_PORT])

# Receive audio from client.
subprocess.Popen(["python3", "audio_stream_client.py", CLIENT_IP, CLIENT_PORT, DEVICE_ID, "44100"])

while(True):
    pass
