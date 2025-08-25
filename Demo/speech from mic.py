# app/record.py
import sounddevice as sd
import soundfile as sf

def record(filename="input.wav", duration=5, fs=16000):
    print("🎙 Recording...")
    audio = sd.rec(int(duration*fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    sf.write(filename, audio, fs)
    print("✅ Saved:", filename)

if __name__ == "__main__":
    record()
    #Hi
