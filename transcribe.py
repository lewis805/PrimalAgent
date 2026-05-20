#!/usr/bin/env python3
import sys, os
os.environ["PATH"] = os.path.expanduser("~/.local/bin:") + os.environ.get("PATH", "")
import whisper

def transcribe(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"].strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: transcribe.py <audio_file>", file=sys.stderr)
        sys.exit(1)
    print(transcribe(sys.argv[1]))
