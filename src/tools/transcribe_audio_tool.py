import whisper
import requests
from io import BytesIO
from pydub import AudioSegment
from utils.constants import GAIA_FILE_ATTACHMENT_URL, GAIA_QUESTION_URL
from utils.constants import DEFAULT_HF_API_URL

class AudioTranscriberTool:
    def convert_audio_to_wav(self, input_file):
        """Converts various audio formats to WAV in memory."""
        # If input is bytes or BytesIO
        if isinstance(input_file, (bytes, BytesIO)):
            audio = AudioSegment.from_file(BytesIO(input_file) if isinstance(input_file, bytes) else input_file)
        else:
            # If input is a file path
            audio = AudioSegment.from_file(input_file)
        
        # Create in-memory WAV file
        wav_io = BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        return wav_io

    def transcribe_audio(self, audio_path):
        """Transcribes speech from an audio file using Whisper."""
        model = whisper.load_model("base")
        # If audio_path is BytesIO, save to temporary file (Whisper requirement)
        if isinstance(audio_path, BytesIO):
            import tempfile
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
                temp_file.write(audio_path.getvalue())
                temp_file.flush()
                result = model.transcribe(temp_file.name)
        else:
            result = model.transcribe(audio_path)
        return result["text"]

    def process_speech_to_text(self, audio_path):
        """Handles the entire speech-to-text process."""

        try:
            response = requests.get(audio_path, stream=True, timeout=30)
            audio_input = BytesIO(response.content)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching audio file: {e}")
            return f"Error fetching audio file: {e}"
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON response from audio endpoint: {e}")
            return f"Error decoding JSON response from audio endpoint: {e}"
        except Exception as e:  
            print(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"
        
        # Convert to WAV if needed
        if isinstance(audio_input, (bytes, BytesIO)):
            audio_file = self.convert_audio_to_wav(audio_input)
        else:
            if not audio_input.endswith(".wav"):
                audio_file = self.convert_audio_to_wav(audio_input)
            else:
                audio_file = audio_input

        transcript = self.transcribe_audio(audio_file)
        return transcript