import whisper

model = whisper.load_model("tiny.en")

result = model.transcribe("C:/Users/VICTUS/Desktop/AudioStream/audio.m4a")

print(result["text"])