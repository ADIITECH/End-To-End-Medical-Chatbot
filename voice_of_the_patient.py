#Step1: Setup Audio recorder (ffmpeg & portaudio)
# ffmpeg, portaudio, pyaudio

import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import logging
import numpy as np
import os

from io import BytesIO
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio_sounddevice(duration=10, output_path="output.mp3", samplerate=44100):
    try:
        logging.info("Recording started. Speak now...")
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()
        logging.info("Recording complete.")

        # Save to WAV first
        wav_path = "temp_output.wav"
        write(wav_path, samplerate, audio_data)

        # Convert to MP3 using pydub
        audio_segment = AudioSegment.from_wav(wav_path)
        audio_segment.export(output_path, format="mp3", bitrate="128k")
        logging.info(f"Audio saved to {output_path}")

        # Clean up temporary WAV file
        os.remove(wav_path)

    except Exception as e:
        logging.error(f"Error during recording: {e}")

# Example usage
# record_audio_sounddevice(duration=10, output_path="patient_voice_test_sounddevice.mp3")
