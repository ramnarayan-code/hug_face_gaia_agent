import whisper

from pydub import AudioSegment

class AudioTranscriberTool:
    def convert_audio_to_wav(self, input_file, output_file="converted.wav"):
        """Converts various audio formats to WAV (if needed)."""
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="wav")
        return output_file

    def transcribe_audio(self, audio_path):
        """Transcribes speech from an audio file using Whisper."""
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result["text"]

    def process_speech_to_text(self, audio_file):
        """Handles the entire speech-to-text process."""
        if not audio_file.endswith(".wav"):
            audio_file = self.convert_audio_to_wav(audio_file)

        transcript = self.transcribe_audio(audio_file)
        return transcript