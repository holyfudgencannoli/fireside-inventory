from vosk import Model, KaldiRecognizer
import wave
import json

MODEL_PATH = "./acoustic_models/vosk-model-en-us-0.22"

wf = wave.open("test.wav", "rb")

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(json.loads(rec.Result()))

print(json.loads(rec.FinalResult()))