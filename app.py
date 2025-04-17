from flask import Flask, render_template, request
from my_assistant import MyAssistant

app = Flask(__name__)
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


if __name__ == '__main__':
    app.run(debug=True)