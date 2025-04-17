from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        transcript = request.form['transcript']
        print(transcript)
    return render_template('index.html', summary = transcript)


if __name__ == '__main__':
    app.run(debug=True)