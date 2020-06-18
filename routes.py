from flask import Flask, render_template, request
import requests
# from flask_dynamic import app

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/tone')
def button_to_tone():
    
    button_number = int(request.args.get("button_number"))
    
    tones = ["C4","B3","A3","G3","F3","E3","D3","C3"]

    return tones[button_number-1]


if __name__ == '__main__':
    app.run(debug=True)
