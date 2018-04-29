#!/usr/bin/env python3
import time
import speech_recognition as sr
from collections import deque
from threading import Thread
try:
	from queue import Queue  # Python 3 import
except ImportError:
	from Queue import Queue  # Python 2 import

m = sr.Microphone()

def calibrate(r):
	with m as source:
		r.adjust_for_ambient_noise(source)

r = sr.Recognizer()

audio_queue = Queue()
command_buffer = deque()

def get_command():
    return list.popleft()

def get_buffer():
    return command_buffer

def recognize_worker():
    # this runs in a background thread
    while True:
        audio = audio_queue.get()  # retrieve the next audio processing job from the main thread
        if audio is None: break  # stop processing if the main thread is done

        # received audio data, now we'll recognize it using CMU Sphinx
        try:
            commands = r.recognize_sphinx(audio)
            print("Sphinx thinks you said " + commands)
            command_buffer.append(commands)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        audio_queue.task_done()  # mark the audio processing job as completed in the queue

calibrate(r)  # calibrate before starting listening process

# start a new thread to recognize audio, while this thread focuses on listening
recognize_thread = Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()
with m as source:
    try:
        while True:  # repeatedly listen for phrases and put the resulting audio on the audio processing job queue
            audio_queue.put(r.listen(source))
    except KeyboardInterrupt:  # allow Ctrl + C to shut down the program
        pass

audio_queue.join()  # block until all current audio processing jobs are done
audio_queue.put(None)  # tell the recognize_thread to stop
recognize_thread.join()  # wait for the recognize_thread to actually stop
