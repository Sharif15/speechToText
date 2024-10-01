'''
This is demonstrating a usage of the speechToText function to transcribe audio files 

'''

import speechToText

user_input = input("Put the path to the audio below:\n")

speechToText.speechToText(user_input,"large")