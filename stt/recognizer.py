from vosk import Model, KaldiRecognizer
import json

class STTRecognizer:
    def __init__(self, model_path="model", sample_rate=16000, grammar=None):
        print(f"Loading model from {model_path}...")
        self.model = Model(model_path)
        self.sample_rate = sample_rate
        self.grammar = grammar

    def create_recognizer(self):
        if self.grammar:
            return KaldiRecognizer(self.model, self.sample_rate, self.grammar)
        return KaldiRecognizer(self.model, self.sample_rate)

    def accept_audio(self, rec, audio_bytes):
        if rec.AcceptWaveform(audio_bytes):
            return json.loads(rec.Result())
        else:
            return json.loads(rec.PartialResult())

    def final_result(self, rec):
        return json.loads(rec.FinalResult())