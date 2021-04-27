import pyaudio
import wave
import sys

# length of data to read.
chunk = 1024
RESPEAKER_INDEX = 1
# validation. If a wave file hasn't been specified, exit.
if len(sys.argv) < 2:
    print("Plays a wave file.\n\n" + "Usage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

# open the file for reading.
wf = wave.open(sys.argv[1], 'rb')

# create an audio object
p = pyaudio.PyAudio()

# open stream based on the wave object which has been input.
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True,
                output_device_index = RESPEAKER_INDEX)

# read data (based on the chunk size)
data = wf.readframes(chunk)
# play stream (looping from beginning of file to the end)
while data:
    # writing to the stream is what *actually* plays the sound.
    stream.write(data)
    data = wf.readframes(chunk)

# cleanup stuff.
stream.close()    
p.terminate()
