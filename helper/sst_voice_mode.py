from openai import OpenAI
# import sounddevice as sd
# import numpy as np
# import io
# import wave
from dotenv import load_dotenv

load_dotenv()
# # OpenAI API key

client = OpenAI()




# # Main function
# def main():
#     audio_buffer = record_audio()  # Record audio from the microphone
#     transcription = transcribe_audio(audio_buffer)  # Transcribe the recorded audio
#     print("Transcription:\n", transcription)

# if __name__ == "__main__":
#     main()







# import sounddevice as sd
# import scipy.io.wavfile as wav
# import numpy as np
# import time
# from openai import OpenAI
# import io

# class AudioRecorder:
#     def __init__(self):
#         self.recording = False
#         self.audio_data = []
#         self.sample_rate = 44100  # Standard sample rate
#         self.client = OpenAI()  # Make sure you've set OPENAI_API_KEY in your environment
        
#     def callback(self, indata, frames, time, status):
#         if self.recording:
#             self.audio_data.extend(indata.copy())
    
#     def record_audio(self):
#         print("Enter 's' to start recording")
#         print("Enter 'p' to pause recording")
#         print("Enter 'q' to quit and save")
        
#         with sd.InputStream(callback=self.callback, 
#                           channels=1,
#                           samplerate=self.sample_rate):
#             while True:
#                 command = input().lower()
                
#                 if command == 's':
#                     print("Recording started...")
#                     self.recording = True
#                     self.audio_data = []
                
#                 elif command == 'p':
#                     if self.recording:
#                         print("Recording paused...")
#                         self.recording = False
                
#                 elif command == 'q':
#                     if self.recording:
#                         self.recording = False
#                     break
    
#     def save_audio(self, filename="recorded_audio.wav"):
#         if len(self.audio_data) > 0:
#             audio_data = np.array(self.audio_data)
#             wav.write(filename, self.sample_rate, audio_data)
#             print(f"Audio saved as {filename}")
#         else:
#             print("No audio data to save")

#     def transcribe_audio(self, audio_file):
#         """
#         Transcribe audio using OpenAI's Whisper model.
        
#         Args:
#             audio_file: Path to the audio file to transcribe
#         Returns:
#             str: Transcribed text
#         """
#         try:
#             with open(audio_file, 'rb') as audio_buffer:
#                 transcription = self.client.audio.transcriptions.create(
#                     model="whisper-1",
#                     file=audio_buffer
#                 )
#                 return transcription.text
#         except Exception as e:
#             print(f"Error during transcription: {e}")
#             return ""

#     def transcribe_audio(self, audio_file):
#         """
#         Transcribe audio using OpenAI's Whisper model.
        
#         Args:
#             audio_file: Path to the audio file to transcribe
#         Returns:
#             str: Transcribed text
#         """
#         try:
#             with open(audio_file, 'rb') as audio_buffer:
#                 transcription = self.client.audio.transcriptions.create(
#                     model="whisper-1",
#                     file=audio_buffer
#                 )
#                 return transcription.text
#         except Exception as e:
#             print(f"Error during transcription: {e}")
#             return ""

# def sst_voice_mode():
#     recorder = AudioRecorder()
    
#     try:
#         # Start recording
#         recorder.record_audio()
        
#         # Save the recording
#         recorder.save_audio()
        
#         # Execute the next part and transcribe
#         transcribed_text = recorder.transcribe_audio("recorded_audio.wav")
#         return (f"{transcribed_text}")
        
#     except KeyboardInterrupt:
#         print("\nRecording interrupted.")
#         recorder.save_audio()




import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import time
from openai import OpenAI
import threading

class AudioRecorder:
    def __init__(self):
        self.recording = False
        self.audio_data = []
        self.sample_rate = 44100  # Standard sample rate
        self.client = OpenAI()  # Make sure you've set OPENAI_API_KEY in your environment
        self.stream = None

    def callback(self, indata, frames, time, status):
        if self.recording:
            self.audio_data.extend(indata.copy())

    def start_recording(self):
        """Start the audio recording."""
        self.recording = True
        self.audio_data = []  # Clear any previous recordings
        self.stream = sd.InputStream(callback=self.callback, channels=1, samplerate=self.sample_rate)
        self.stream.start()

    def stop_recording(self):
        """Stop the audio recording."""
        self.recording = False
        if self.stream is not None:
            self.stream.stop()
            self.stream.close()

    def save_audio(self, filename="recorded_audio.wav"):
        """Save the recorded audio to a file."""
        if len(self.audio_data) > 0:
            audio_data = np.array(self.audio_data)
            wav.write(filename, self.sample_rate, audio_data)
            print(f"Audio saved as {filename}")
        else:
            print("No audio data to save")

    def transcribe_audio(self, audio_file):
        """Transcribe the saved audio using OpenAI's Whisper model."""
        try:
            with open(audio_file, 'rb') as audio_buffer:
                transcription = self.client.audio.transcriptions.create(
                    model="whisper-1", file=audio_buffer
                )
                return transcription.text
        except Exception as e:
            print(f"Error during transcription: {e}")
            return ""


def sst_voice_mode():
    recorder = AudioRecorder()

    # add button here to get the recording start // rn uses enter 
    # ig this @app.route('/start_recording', methods=['POST'])

    print("Press Enter to start recording.")
    input()  # Wait for Enter key

    recorder.start_recording()  # Start the audio recording



    # add button here to stop the recording
    # ig @app.route('/stop_recording', methods=['POST'])
    print("Recording... Press Enter again to stop and transcribe.")
    input()  # Wait for Enter again


    recorder.stop_recording()  # Stop the recording

    #ig u would need to save this file 
    recorder.save_audio()  # Save the recording

    # Transcribe the recorded audio
    transcribed_text = recorder.transcribe_audio("recorded_audio.wav")
    return transcribed_text


