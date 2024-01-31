import whisper

model = whisper.load_model("medium")
result = model.transcribe('audio.mp3')['text']

with open('audio.txt', 'w') as f:
    f.write(result)

print(result)
