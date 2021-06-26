import pyaudio
import socket
import select
import os
import sys


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = int(sys.argv[1]) # 44100, 16000
CHUNK = 512
PAUSEFILE = '.audio.bot.pause'

audio = pyaudio.PyAudio()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', int(sys.argv[2])))
serversocket.listen(5)


def callback(in_data, frame_count, time_info, status):
    for s in read_list[1:]:
        # Creating this file will halt sending data to all devices.
        if not os.path.isfile(PAUSEFILE):
            s.send(in_data)
    return (None, pyaudio.paContinue)


# Start streaming.
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=callback)

read_list = [serversocket]
print ("Streaming...")

try:
    while True:
        readable, writable, errored = select.select(read_list, [], [])
        for s in readable:
            if s is serversocket:
                (clientsocket, address) = serversocket.accept()
                read_list.append(clientsocket)
                print ("Connection from ()".format(address))
            else:
                data = s.recv(1024)
                if not data:
                    read_list.remove(s)
except KeyboardInterrupt:
    pass

print ("Finished streaming.")

# Clean up.
serversocket.close()
stream.stop_stream()
stream.close()
audio.terminate()
