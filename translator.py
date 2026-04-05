import whisper
from moviepy.editor import VideoFileClip, AudioFileClip
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# -------------------------------
# CONFIG
# -------------------------------
input_video = "/home/openbravo/voice/videos/dark_psychology_visible_images.mp4"
target_language = "hi"   # hi = Hindi, mr = Marathi, en = English

audio_file = "audio.wav"
translated_audio = "translated_audio.mp3"
output_video = "translated_video.mp4"

# -------------------------------
# STEP 1: Extract Audio
# -------------------------------
print("Extracting audio from video...")

video = VideoFileClip(input_video)
video.audio.write_audiofile(audio_file)

# -------------------------------
# STEP 2: Speech to Text
# -------------------------------
print("Transcribing audio...")

model = whisper.load_model("base")
result = model.transcribe(audio_file)

original_text = result["text"]

print("Original Text:")
print(original_text)

# -------------------------------
# STEP 3: Translate Text
# -------------------------------
print("Translating text...")

translated_text = GoogleTranslator(
    source="auto",
    target=target_language
).translate(original_text)

print("Translated Text:")
print(translated_text)

# -------------------------------
# STEP 4: Text to Speech
# -------------------------------
print("Generating translated speech...")

tts = gTTS(text=translated_text, lang=target_language)
tts.save(translated_audio)

# -------------------------------
# STEP 5: Replace Video Audio
# -------------------------------
print("Merging translated audio with video...")

new_audio = AudioFileClip(translated_audio)

final_video = video.set_audio(new_audio)

final_video.write_videofile(
    output_video,
    codec="libx264",
    audio_codec="aac"
)

print("Done! Output video saved:", output_video)