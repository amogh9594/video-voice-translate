import whisper
from moviepy.editor import VideoFileClip, AudioFileClip
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# -------------------------------
# CONFIG
# -------------------------------
input_video = "/home/openbravo/voice/videos/dark_psychology_visible_images.mp4"
target_language = "gu"

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

segments = result["segments"]

# -------------------------------
# STEP 3: Translate + Build Text
# -------------------------------
print("Translating text...")

translated_full_text = ""

for seg in segments:
    text = seg["text"]
    
    translated = GoogleTranslator(
        source="auto",
        target=target_language
    ).translate(text)
    
    translated_full_text += translated + " "

print("Translated Text:")
print(translated_full_text)

# -------------------------------
# STEP 4: Text to Speech
# -------------------------------
print("Generating Gujarati speech...")

tts = gTTS(text=translated_full_text, lang=target_language)
tts.save(translated_audio)

# -------------------------------
# STEP 5: Merge Audio with Video
# -------------------------------
print("Merging translated audio with video...")

new_audio = AudioFileClip(translated_audio)

# OPTIONAL: match duration
new_audio = new_audio.set_duration(video.duration)

final_video = video.set_audio(new_audio)

final_video.write_videofile(
    output_video,
    codec="libx264",
    audio_codec="aac"
)

print("✅ Done! Output video saved:", output_video)