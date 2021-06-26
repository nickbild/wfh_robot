import pyaudio
import socket
import sys

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = sys.argv[3]
CHUNK = 512

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK, output_device_index=int(sys.argv[3]))

try:
    while True:
        data = s.recv(CHUNK)
        stream.write(data)
except KeyboardInterrupt:
    pass

print('Shutting down')
s.close()
stream.close()
audio.terminate()

