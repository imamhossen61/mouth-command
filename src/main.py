import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to process voice commands
def process_command(command):
    print(f"Executing command: {command}")
    # Add your code to execute the desired action based on the command

# Main loop for listening to voice commands
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Speech Recognition
    command = recognizer.recognize_google(audio)
    print(f"You said: {command}")
    process_command(command)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
