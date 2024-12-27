import sounddevice as sd
import numpy as np
import io
from elevenlabs import ElevenLabs
import os 

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('ELEVEN_API_KEY')


# Function to play the audio
def voice_mode(text_input):
    # Initialize ElevenLabs client
    client = ElevenLabs(api_key)
    
    
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
