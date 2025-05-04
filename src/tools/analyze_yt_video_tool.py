import requests

from pytubefix import YouTube
from io import BytesIO
from tools.transcribe_audio_tool import AudioTranscriberTool

class AnalyzeYTVideoTool:
    """
    A tool for analyzing YouTube videos by downloading and transcribing their audio content.
    This class provides functionality to download YouTube video audio and analyze it by
    transcribing the audio content and combining it with the video description.
    Methods
    -------
    analyze(url: str) -> str
        Analyzes a YouTube video by transcribing its audio and combining with description.
            url (str): The URL of the YouTube video to analyze
            str: Combined transcription and video description
        Raises:
            Exception: If there is an error downloading or processing the video
    Private Methods
    --------------
    __download_audio(url: str) -> YouTube| BytesIO
        Downloads YouTube video audio as BytesIO object.
            url (str): YouTube video URL
            Tuple[YouTube, BytesIO]: YouTube object and BytesIO containing audio data
        Raises:
            Exception: If download fails
    """
    def __download_audio(self, url: str) -> YouTube| BytesIO:
        try:
            # Create YouTube object
            yt = YouTube(url)
            
            # Get audio stream
            audio_stream = yt.streams.filter(only_audio=True).first()
         
            # Download the audio content into BytesIO
            response = requests.get(audio_stream.url, stream=True)
            response.raise_for_status()
            
            # Create BytesIO object and write content
            audio_bytes = BytesIO()
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    audio_bytes.write(chunk)
            
            # Reset pointer to start of BytesIO object
            audio_bytes.seek(0)
            
            return yt, audio_bytes
            
        except Exception as e:
            print(f"Error downloading YouTube audio: {str(e)}")
            raise Exception(f"Failed to download YouTube audio: {str(e)}")

    def analyze(self, url: str) -> str:
        yt, audio = self.__download_audio(url)
        return AudioTranscriberTool().transcribe_audio_file(audio) + yt.description
