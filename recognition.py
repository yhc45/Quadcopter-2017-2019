import time
import speech_recognition as sr

m = sr.Microphone()

def calibrate(r):
	with m as source:
		r.adjust_for_ambient_noise(source)

def initialize_recognizer():
	r = sr.Recognizer()
	calibrate(r)
	return r

r = initialize_recognizer()

def get_voice_command():
	# obtain audio from the microphone
	with sr.Microphone() as source:
		print("Listening...")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	# recognize speech using Sphinx
	output = None
	try:
		output = r.recognize_sphinx(audio)
		print("Sphinx thinks you said " + output)
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))

	return output

# get_voice_command()

def callback(r, audio):
	output = None
	try:
		output = r.recognize_sphinx(audio)
		print("Sphinx thinks you said " + output)
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))

stop_listening = r.listen_in_background(m, callback)

for _ in range(150): time.sleep(0.1)

stop_listening(wait_for_stop=False)
