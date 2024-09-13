# get the Library used for speech to text

import whisper

import re #to handle spliting the text

import time #used for performing test on code efficiency.

# "/Users/sharifislam/Documents/Github/speechToText/Surah_al_baqarah.band/Media/Audio Files/Untitled#18.wav"

def writeHeader(fileName,modelName,taskTime,outPutFile):
    file = open(fileName, "a")
    file.write("\n\n")
    for i in range(10):
        file.write("#")
    file.write("\n")
    file.write("\n The Model Used: " + modelName)
    file.write("\n Time it took to transcribe: " + taskTime + " mins")
    file.write("\n The text file is at: " + outPutFile + "\n")
    for i in range(10):
        file.write("#")
    file.write("\n\n")
    


#used to write the result string to files
def writeOutput(text,fileName):
    
    openFile = fileName + "_transcript.txt" 
    outputFile = open(openFile,"w")

    separators = ".,?"
    
    # Pattern to split on either separators or capital letters
    pattern = f"[{re.escape(separators)}] | (?<!\\bI\\b)(?<!\\bI')(?=[A-Z])"

    outputText = re.split(pattern,result["text"])

    for text in outputText :
        outputFile.write(text + "\n")

    outputFile.close()
    
    return openFile
    
#Start of main Code

modelName = "large"

model = whisper.load_model(modelName)

PATH = "testAudio/Solitude.wav"

filename = PATH.split('/')[-1].split('.wav')[0]

filename = filename.replace(" ", "_")

startTime = time.time() #start of the aplication

result = model.transcribe(PATH) # the Step that converts the audio to text

endTime = time.time() #End of the task 

totalTime = endTime - startTime
totalTime /= 60 
totalTime = str(totalTime)

outPutDestination = writeOutput(result["text"],filename)
writeHeader(outPutDestination,modelName,totalTime,outPutDestination)

#writes down the origial language transcription if not english
if result["language"] != "en":
    result = model.transcribe(PATH,task = "translate")
    writeOutput(result["text"],filename + "_" + result["language"])

print("The transcription is finished!!")