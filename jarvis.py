import pyaudio;
import wave;
import pyttsx3;
import speechRecognition as sr;
import webbrowser;

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voice[0].id);
 
def speak(words):
    engine.say(words);
    engine.runAndWait();

def setAIvoice(choice):    
    engine.setProperty('voice', voice[choice].id);

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        words = r.listen(source)


chunk = 1024      # Each chunk will consist of 1024 samples
sample_format = pyaudio.paInt16      # 16 bits per sample
channels = 2      # Number of audio channels
fs = 44100        # Record at 44100 samples per second
time_in_seconds = 10
filename = "soundsample.wav"
 
p = pyaudio.PyAudio()  # Create an interface to PortAudio
 
print('-----Now Recording-----')
 
#Open a Stream with the values we just defined
stream = p.open(format=sample_format,
                channels = channels,
                rate = fs,
                frames_per_buffer = chunk,
                input = True)
 
frames = []  # Initialize array to store frames
 
# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * time_in_seconds)):
    data = stream.read(chunk)
    frames.append(data)
 
# Stop and close the Stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()
 
print('-----Finished Recording-----')
 
# Open and Set the data of the WAV file
file = wave.open(filename, 'wb')
file.setnchannels(channels)
file.setsampwidth(p.get_sample_size(sample_format))
file.setframerate(fs)
 
#Write and Close the File
file.writeframes(b''.join(frames))
file.close()

def main():
    
