'''
This Python script records audio from the computer's microphone and saves it as a .wav file.
The user can specify the recording duration and file name, or default values are used if no input is provided.
The final file name is also copied to the clipboard.

Default settings: 
    16-bit mono audio, 
    44.1 kHz sampling, 
    15 seconds recording time,
    and "capturedAudio/recorded_audio.wav" as the default file name.
    
User input: Optional inputs for recording duration and file name.

Clipboard: The saved file name is automatically copied to the clipboard.
'''

import pyaudio
import wave
import pyperclip  # To clip the captured audio filename to the clipboard

# Default parameters for the audio recording
DEFAULT_FORMAT = pyaudio.paInt16  # 16-bit resolution
DEFAULT_CHANNELS = 1              # Mono channel
DEFAULT_RATE = 44100              # Sampling rate (44.1 kHz)
DEFAULT_CHUNK = 1024              # Size of each buffer
DEFAULT_RECORD_SECONDS = 15       # Default recording time in seconds
DEFAULT_OUTPUT_FILENAME = "capturedAudio/recorded_audio.wav"  # Default output file name

# Ask the user for recording duration
user_record_time = input(f"Enter the recording duration in seconds (default is {DEFAULT_RECORD_SECONDS}): ")
if user_record_time.strip() == "":
    record_seconds = DEFAULT_RECORD_SECONDS
else:
    record_seconds = int(user_record_time)

# Ask the user for the name of the file to save to
user_output_file = input(f"Name the audio file (default is {DEFAULT_OUTPUT_FILENAME}): ").strip()

# If the user didn't provide a file name, use the default
if user_output_file == "":
    output_filename = DEFAULT_OUTPUT_FILENAME
else:
    output_filename = "capturedAudio/" + user_output_file + ".wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

print("Starting Now...")

# Start recording
stream = audio.open(format=DEFAULT_FORMAT, channels=DEFAULT_CHANNELS,
                    rate=DEFAULT_RATE, input=True,
                    frames_per_buffer=DEFAULT_CHUNK)

print(f"Recording for {record_seconds} seconds...")

frames = []

# Capture the audio data
for _ in range(0, int(DEFAULT_RATE / DEFAULT_CHUNK * record_seconds)):
    data = stream.read(DEFAULT_CHUNK)
    frames.append(data)

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the captured data to a .wav file
with wave.open(output_filename, 'wb') as wf:
    wf.setnchannels(DEFAULT_CHANNELS)
    wf.setsampwidth(audio.get_sample_size(DEFAULT_FORMAT))
    wf.setframerate(DEFAULT_RATE)
    wf.writeframes(b''.join(frames))

# Copy the file name to clipboard
pyperclip.copy(output_filename)

print(f"Audio saved as {output_filename} and copied to clipboard.")
