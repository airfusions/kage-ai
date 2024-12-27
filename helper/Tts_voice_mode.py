#for collab

# from elevenlabs import ElevenLabs
# from IPython.display import Audio, display

# # Function to generate and play audio
# def voice_mode(input):
#     # Initialize ElevenLabs client
#     client = ElevenLabs(
#         api_key="sk_71cf8d748b71726b149d5b02a33aef16236280cc31544df8",
#     )
    
#     # Generate the audio as a stream
#     response = client.text_to_speech.convert(
#         voice_id="JBFqnCBsd6RMkjVDRZzb",
#         output_format="mp3_44100_128",
#         text=input,
#         model_id="eleven_multilingual_v2",
#     )
    
#     # Concatenate the chunks of audio data into a single byte object
#     audio_data = b"".join(response)
    
#     # Play the audio automatically
#     display(Audio(audio_data, rate=44100, autoplay=True))

# # Call the function


# # for terminal with saving the file 

# from elevenlabs import ElevenLabs
# from io import BytesIO
# from playsound import playsound

# # Function to generate and play audio directly from memory
# def voice_mode(input):
#     # Initialize ElevenLabs client
#     client = ElevenLabs(
#         api_key="sk_71cf8d748b71726b149d5b02a33aef16236280cc31544df8",
#     )
    
#     # Generate the audio as a stream
#     response = client.text_to_speech.convert(
#         voice_id="JBFqnCBsd6RMkjVDRZzb",
#         output_format="mp3_44100_128",
#         text=input,
#         model_id="eleven_multilingual_v2",
#     )
    
#     # Concatenate the chunks of audio data into a single byte object
#     audio_data = b"".join(response)
    
#     # Write the audio data to a BytesIO object and play it
#     audio_bytes = BytesIO(audio_data)
    
#     # Using playsound to play the audio directly (requires a file path)
#     with open("temp_audio.mp3", "wb") as f:
#         f.write(audio_data)
#     playsound("temp_audio.mp3")

# # Call the function

import sounddevice as sd
import numpy as np
import io
from elevenlabs import ElevenLabs

# Function to play the audio
def voice_mode(text_input):
    # Initialize ElevenLabs client
    client = ElevenLabs(api_key="sk_71cf8d748b71726b149d5b02a33aef16236280cc31544df8")
    
    # Generate the audio as a stream
    response = client.text_to_speech.convert(
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        output_format="mp3_44100_128",
        text=text_input,
        model_id="eleven_multilingual_v2"
    )
    
    # Extract the content (audio data) from the generator
    audio_data = b"".join(response)
    
    # Read the audio data into a BytesIO buffer
    audio_bytes = io.BytesIO(audio_data)

    # Convert the MP3 data into a numpy array using soundfile or other methods (MP3 decoding)
    # You may need a library like pydub or ffmpeg to decode MP3 into PCM data
    import soundfile as sf
    
    # Read MP3 data and convert to PCM
    audio_array, samplerate = sf.read(audio_bytes, dtype='int16')

    # Play the audio using sounddevice
    sd.play(audio_array, samplerate=samplerate)
    sd.wait()  # Wait until the audio is done playing

# Call the function
