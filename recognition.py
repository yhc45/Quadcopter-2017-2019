import speech_recognition as sr

r = sr.Recognizer()

def get_voice_command():
	# obtain audio from the microphone
	with sr.Microphone() as source:
		print("Listening...")
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

get_voice_command()
