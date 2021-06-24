import subprocess


# Start up the camera in the background.
subprocess.Popen(["python3", "image_capture_loop.py"])

# Start simple web server.
subprocess.Popen(["python3", "web_server.py"])
