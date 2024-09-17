# get the Library used for speech to text

import whisper

import re #to handle spliting the text

import time #used for performing test on code efficiency.

#used to try and use apple gpu to process 

import torch

'''
@author Sharif Islam

Name : speechToText

Parameters : 
    modelName : The pre-trained model you want to use of Whisper. 
        Avalable options: "tiny.en" , "tiny" , "base" , "base.en", "small", "small.en" , "medium.en" , "medium" ,
                          "large" , "large-v1" , "large-v2" , "large-v3"
    audioPath : The path to the audio file you want to implement
    
Purpose : 

'''

def speechToText(modelName,audioPath):
    
    
    #provide diagnostics info for a given transcription     
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
        
        # Regular expression to match punctuation marks or a capital letter that's not "I"
        pattern = r'(?<=[.,?])\s+|(?<!\w)\b(?!I\b)(?=[A-Z])' # I DO not know how is string manipulation works

        outputText = re.split(pattern,result["text"])
        
        outputText = [part for part in outputText if part]

        for text in outputText :
            if text is not None:
                outputFile.write(text + "\n")

        outputFile.close()
        
        return openFile
        
    #Start of main Code transcriber code
    
    model = whisper.load_model(modelName) # modelName is expressed when the function is called

    # PATH = "testAudio/Solitude.wav"
    
    PATH = audioPath

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

    #writes down the transilation if the audio was not in english
    if result["language"] != "en":
        result = model.transcribe(PATH,task = "translate")
        writeOutput(result["text"],filename + "_" + result["language"] + "_to_en")

    print("The transcription is finished!!")
    
speechToText("large","testAudio/mañana · Tainy · Young Miko · The Marias.wav")