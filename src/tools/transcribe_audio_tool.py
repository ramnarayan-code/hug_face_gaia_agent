import whisper
import requests

from io import BytesIO
from pydub import AudioSegment

class AudioTranscriberTool:
    """
    AudioTranscriberTool class provides functionality to transcribe audio files to text.
    This class uses the Whisper model to perform audio transcription and supports both local
    audio files and audio files from URLs. It can handle various audio formats and converts
    them to WAV format internally for processing.
    Attributes:
        audio_model: A loaded Whisper model instance used for transcription.
    Methods:
        transcribe_audio_file(audio_file_path: str) -> str:
            Transcribes a local audio file to text.
        transcribe_audio_from_url(audio_file_url: str) -> str:
            Transcribes an audio file from a given URL to text.
    Private Methods:
        __get_audio_object(input_file: Union[str, bytes, BytesIO]) -> AudioSegment:
            Creates an AudioSegment object from various input types.
        __convert_audio_to_wav(audio: AudioSegment) -> BytesIO:
            Converts audio to WAV format in memory.
        __transcribe_audio(audio: BytesIO) -> str:
            Performs the actual transcription using Whisper model.
    Raises:
        requests.exceptions.RequestException: If there's an error fetching audio from URL
        requests.exceptions.JSONDecodeError: If there's an error decoding JSON response
        Exception: For other unexpected errors during transcription
    """
   
    def __init__(self):
        self.audio_model = whisper.load_model("base")

    def __get_audio_object(self, input_file):
        # If input is bytes or BytesIO
        if isinstance(input_file, (bytes, BytesIO)):
            return AudioSegment.from_file(BytesIO(input_file) if isinstance(input_file, bytes) else input_file)
        else:
            # If input is a file path
            return AudioSegment.from_file(input_file)

    def __convert_audio_to_wav(self, audio) -> BytesIO: 
        # Create in-memory WAV file
        wav_io = BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        return wav_io

    def __transcribe_audio(self, audio) -> str:
        # If audio_path is BytesIO, save to temporary file (Whisper requirement)
        import tempfile

        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
            temp_file.write(audio.getvalue())
            temp_file.flush()
            result = self.audio_model.transcribe(temp_file.name)
        
        return result["text"]

    def transcribe_audio_file(self, audio_file: str | BytesIO) -> str:
        try:
            if isinstance(audio_file, str):
                if not audio_file.endswith(".wav"):
                    wav_audio_content = self.__convert_audio_to_wav(self.__get_audio_object(audio_file))
                else:
                    wav_audio_content = self.__get_audio_object(audio_file)
            else:
                wav_audio_content = self.__convert_audio_to_wav(self.__get_audio_object(audio_file))

            return self.__transcribe_audio(wav_audio_content)
        except Exception as e:  
            print(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"

    def transcribe_audio_from_url(self, audio_file_url) -> str:
        try:
            response = requests.get(audio_file_url, stream=True, timeout=30)
            
            audio_object = self.__get_audio_object(BytesIO(response.content))
            wav_audio_content = self.__convert_audio_to_wav(audio_object)

            return self.__transcribe_audio(wav_audio_content)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching audio file: {e}")
            return f"Error fetching audio file: {e}"
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON response from audio endpoint: {e}")
            return f"Error decoding JSON response from audio endpoint: {e}"
        except Exception as e:  
            print(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"

       