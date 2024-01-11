import os
import shutil
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from morse import Morse
from weather import Weather
from text_to_speech import get_audio
# from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "123123123123dasdasd"

app.config['AUDIO_FOLDER'] = 'UPLOADS/audio'

morse = Morse()
weather_instance = Weather()


def empty(path):
    folder = f'/UPLOADS/{path}'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


@app.route('/', methods=["POST", "GET"])
def homepage():
    return render_template("index.html")


@app.route('/morse', methods=["POST"])
def get_morse():
    if request.method == "POST":
        morse.reset()
        data = request.form.get("text")
        morse_output = morse.to_morse(data)
        return jsonify({"morse_output": morse_output})


@app.route('/weather', methods=["POST"])
def weather():
    if request.method == "POST":
        temperature, condition, condition_icon, city, country = weather_instance.get_weather()
        response_data = {"temperature": temperature, "condition": condition, "icon": condition_icon, "city": city,
                         "country": country}
        return jsonify(response_data)


@app.route('/upload-text', methods=['POST'])
def upload_text():
    if request.method == "POST":
        text = request.form.get("text")
        if len(text) != 0:
            audio_url = get_audio(text)
            if audio_url:
                return jsonify({"audio_url": audio_url}), 200
            else:
                return jsonify({"error": "Failed to generate audio"}), 500
        else:
            return jsonify({"error": "Nothing typed yet"}), 400


@app.route('/UPLOADS/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)


if __name__ == "__main__":
    app.run()
