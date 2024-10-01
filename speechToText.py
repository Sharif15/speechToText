# get the Library used for speech to text

import whisper

import re #to handle spliting the text

import time #used for performing test on code efficiency.

'''
@author Sharif Islam

Name : speechToText

Parameters : 
    modelName : The pre-trained model you want to use from Whisper. 
        Available options: "tiny.en" , "tiny" , "base" , "base.en", "small", "small.en" , "medium.en" , "medium" ,
                           "large" , "large-v1" , "large-v2" , "large-v3"
    audioPath : The path to the audio file you want to implement
    
Purpose : Takes an audio file as an input and produces a text file with the transcription of the audio using the openai-whisper library.

Returns: 
    str: The path to the generated transcript file.
    
'''

def speechToText(audioPath: str, modelName: str = "base") -> str:
    
    #provide diagnostics info for a given transcription     
    def writeHeader(fileName: str, modelName: str, taskTime):
        with open(fileName, "a") as file:
            file.write("\n\n")
            file.write("#" * 10 + "\n")
            file.write("\n The Model Used: " + modelName)
            file.write("\n Time it took to transcribe: " + taskTime + " mins")
            file.write("\n The text file is at: " + fileName + "\n")
            file.write("#" * 10 + "\n\n")

    #used to write the result string to files
    def writeOutput(text,fileName):
        
        openFile = fileName + "_transcript.txt" 
        with open(openFile,"w") as outputFile:
        
            # Regular expression to match punctuation marks or a capital letter that's not "I"
            pattern = r'(?<=[.,?])\s+|(?<!\w)\b(?!I\b)(?=[A-Z])' # I DO not know how is string manipulation works

            outputText = re.split(pattern,result["text"])
            
            outputText = [part for part in outputText if part] # Prints out each section in the array if it's not null

            for text in outputText :
                if text is not None:
                    outputFile.write(text + "\n")  
                    
        return openFile
        
    #Start of main Code transcriber code
    
    model = whisper.load_model(modelName) # modelName is expressed when the function is called

    # PATH = "testAudio/Solitude.wav"
    
    PATH = audioPath

    filename = PATH.split('/')[-1].split('.wav')[0]

    filename = filename.replace(" ", "_")

    startTime = time.time() #start of the aplication # Only for performance tracking

    result = model.transcribe(PATH) # the Step that converts the audio to text

    endTime = time.time() #End of the task 

    totalTime = endTime - startTime # Performance tracking 
    totalTime /= 60                 # Performance tracking 
    totalTime = str(totalTime)      # Performance tracking 

    outPutDestination = writeOutput(result["text"],filename)
    writeHeader(outPutDestination,modelName,totalTime)

    print("The transcription is finished!!")
    print("The transcript file is : " + outPutDestination)
    return outPutDestination
    