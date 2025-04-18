import os
from flask import Flask, request, render_template
from faster_whisper import WhisperModel # Import the WhisperModel class
from my_assistant import MyAssistant

# --- Flask App Setup ---
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model_size = "tiny.en" # Or "base.en" for slightly better accuracy

device_type = "cpu"
compute_type = "int8"

try:
    print(f"Loading Faster-Whisper model: {model_size} (device={device_type}, compute={compute_type})...")
    model = WhisperModel(model_size, device=device_type, compute_type=compute_type)
    print("Faster-Whisper model loaded successfully.")
except Exception as e:
    print(f"Error loading Faster-Whisper model: {e}")
    model = None


@app.route('/', methods=['GET', 'POST'])
def index():
    Assistant = MyAssistant()
    transcript = ''
    summary = ''
    if request.method == 'POST':
        transcript = request.form['transcript']
        print(transcript)
        summary = Assistant.generate(transcript)
    return render_template('index.html', summary=summary)

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if not model: # Check if model failed to load
         return "Error: Transcription model not available", 503

    if 'audio_blob' not in request.files:
        return "Error: No audio blob found", 400

    audio_file = request.files['audio_blob']
    filename = "temp_recording.webm" # Simple fixed name
    save_path = os.path.join(UPLOAD_FOLDER, filename)

    try:
        audio_file.save(save_path)
        print(f"Audio saved: {save_path}")

        # --- Transcription using Faster-Whisper ---
        try:
            segments, info = model.transcribe(save_path, beam_size=5)

            print(f"Detected language '{info.language}' with probability {info.language_probability}")

            full_transcript = "".join(segment.text for segment in segments).strip()

            print(f"Transcription: {full_transcript}")
            #  delete the file after processing
            os.remove(save_path)
            return full_transcript, 200 # Return plain text transcript

        except Exception as e:
            print(f"Error during transcription: {e}")
            # delete file on error
            if os.path.exists(save_path): os.remove(save_path)
            return f"Error during transcription: {e}", 500

    except Exception as e:
        print(f"Error saving file: {e}")
        return f"Error saving file: {e}", 500

if __name__ == '__main__':
    # Model loaded above
    app.run(debug=True, host='0.0.0.0', port=5000) # Set debug=False for production