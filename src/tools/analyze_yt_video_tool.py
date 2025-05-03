import requests

from pytubefix import YouTube
from io import BytesIO
from tools.transcribe_audio_tool import AudioTranscriberTool

class AnalyzeYTVideoTool:

    def __download_audio(self, url: str) -> BytesIO:
        """
        Downloads YouTube audio as BytesIO object.
        
        Args:
            url: YouTube video URL
            
        Returns:
            BytesIO object containing the audio data
        """
        try:
            # Create YouTube object
            yt = YouTube(url)
            
            # Get audio stream
            audio_stream = yt.streams.filter(only_audio=True).first()
            
            # Get the direct URL for the audio stream
            audio_url = audio_stream.url
            
            # Download the audio content into BytesIO
            response = requests.get(audio_url, stream=True)
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
        return AudioTranscriberTool().transcribe_audio(audio) + yt.description
