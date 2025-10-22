from vosk import Model, KaldiRecognizer
import sys, json, os, sounddevice as sd

def ouvir_comando(duracao=5):
    if not os.path.exists("voz/model"):
        return "Modelo VOSK não encontrado"
    model = Model("voz/model")
    rec = KaldiRecognizer(model, 16000)
    def callback(indata, frames, time, status):
        if status:
            print(status)
        if rec.AcceptWaveform(indata):
            return True
    print("🎤 Ouvindo comando...")
    recording = sd.rec(int(duracao*16000), samplerate=16000, channels=1, dtype='int16')
    sd.wait()
    if rec.AcceptWaveform(recording):
        result = rec.Result()
        text = json.loads(result).get("text","")
        return text
    return ""
