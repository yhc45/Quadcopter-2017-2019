# Quadcopter-2017-2019-
Annual Project Quadcopter 2017-2019

## Voice Recognition
Voice recognition is done using the [CMU PocketSphinx](https://github.com/bambocher/pocketsphinx-python) API through the [Speech_Recognition](https://github.com/Uberi/speech_recognition) library

## TODO

- ~~Get CMU Pocket Sphinx to work~~
- Get voice recognition as a background thread (should be parsing audio as new audio comes in -- no waiting between words)
- Store parsed results as a string in a list (buffer)
- Create function to return contents in buffer
- Create function to return first item in buffer
- Cut down on number of commands?

## Voice Commands

- Quadcopter names:
	1. Red
	2. Yellow
	3. Blue
	4. Green
- Movement:
	1. Move Left
	2. Move Right
	3. Move Up
	4. Move Down
	5. Move Forward
	6. Move Backward
- Rotation:
	1. Rotate Right
	2. Rotate Left
- Units:
	1. Meters?
	2. Feet?
- Calibrate
- Heal

## Extras
- Competition is in 8 minutes
- [Speech recognizer features](https://github.com/Uberi/speech_recognition/blob/master/examples/special_recognizer_features.py)
