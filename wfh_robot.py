import subprocess
import os


CLIENT_IP = "192.168.1.113"
PORT = 4445


# Initially, make sure robot is NOT muted.
os.system("rm -f .audio.bot.pause")

# Start up the camera in the background.
subprocess.Popen(["python3", "image_capture_loop.py"])

# Start simple web server.
subprocess.Popen(["python3", "web_server.py"])

# Stream audio to client.
subprocess.Popen(["python3", "audio_stream_server.py", "16000"])

# Receive audio from client.
subprocess.Popen(["python3", "audio_stream_client.py", CLIENT_IP, PORT, "44100"])

while(True):
    pass
