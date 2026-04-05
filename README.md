# video-voice-translate

### Installation

### Based on the uploaded Python script that extracts audio from a video, converts speech to text,

### translates the transcript into Gujarati, generates Gujarati speech, and merges that speech back into the

### video.

## 1. What this script does

### This script creates a translated version of an existing video. It reads a source video, extracts its audio,

### transcribes the speech using Whisper, translates the spoken text into Gujarati, converts the translated

### text into speech, and finally replaces the original video audio with the new Gujarati narration.

```
Step Purpose
1 Load the input video file
2 Extract audio from the video into audio.wav
3 Use Whisper to transcribe speech into text segments
4 Translate each segment into Gujarati
5 Combine all translated text into one long string
6 Convert translated text into Gujarati speech using gTTS
7 Attach the new audio to the original video and export translated_video.mp
```
## 2. Required Python libraries

- whisper - converts spoken audio into text.
- moviepy - reads the video file, extracts audio, and writes the final video.
- deep-translator - translates transcribed text into the target language.
- gTTS - converts translated text into spoken audio.
- os - standard Python library used for file/path related tasks. This one does not need installation.

## 3. Installation commands

### Install the required packages with pip. The script also depends on FFmpeg, because video/audio

### processing and Whisper commonly need it to read and write media files correctly.

pip install openai-whisper moviepy deep-translator gTTS
# Check FFmpegffmpeg -version

# If FFmpeg is missing on Ubuntu/Debiansudo apt update
sudo apt install ffmpeg

## 4. Important configuration values in the script


```
Variable Meaning
input_video Path of the original video file that will be processed.
target_language Language code for translation and text-to-speech. Here it is gu, which means Gujarati.
audio_file Temporary extracted audio file name: audio.wav
translated_audio Generated translated speech file: translated_audio.mp
output_video Final exported translated video: translated_video.mp
```
## 5. Code flow explained line by line

### Import section: The script imports all libraries needed for speech recognition, translation,

### text-to-speech, video processing, and file handling.

### Video loading: VideoFileClip(input_video) opens the video so the script can read its audio and later

### write a modified version.

### Audio extraction: video.audio.write_audiofile(audio_file) exports the original spoken soundtrack into a

### WAV file.

### Whisper model loading: whisper.load_model("base") loads the base Whisper model. Bigger models

### can improve accuracy but use more memory and time.

### Transcription: model.transcribe(audio_file) converts the extracted speech into text and returns

### segmented results.

### Segment loop: The for loop reads each transcribed text segment separately. This is useful because

### shorter translation chunks are usually more stable than translating one huge block at once.

### Translation: GoogleTranslator(source="auto", target=target_language).translate(text) detects the

### source language automatically and translates each segment into Gujarati.

### Text merge: Each translated segment is appended to translated_full_text so one final Gujarati

### paragraph is created for speech synthesis.

### Text to speech: gTTS(text=translated_full_text, lang=target_language) generates Gujarati audio and

### saves it as an MP3 file.

### Audio replacement: AudioFileClip(translated_audio) loads the new narration and

### video.set_audio(new_audio) replaces the original soundtrack.

### Final export: final_video.write_videofile(...) writes the finished MP4 video using libx264 for video and

### AAC for audio.

## 6. Output files created by the script

- audio.wav - extracted original audio from the source video.
- translated_audio.mp3 - Gujarati speech generated from translated text.
- translated_video.mp4 - final video with Gujarati narration.

## 7. Practical notes


- This script translates the full transcript and creates one long audio narration. It does not preserve
    sentence-by-sentence timing or lip sync.
- The line new_audio = new_audio.set_duration(video.duration) forces the translated audio to match
    the video duration. If the generated speech is naturally shorter or longer, the pacing may feel off.
- The script assumes the target language code used in translation and gTTS is supported correctly.
- For better quality, subtitle-style timing or per-segment audio generation would be more accurate than
    one single combined narration track.



