from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_image():
    text = request.form.get('text')
    # Rest of the conversion logic goes here

if __name__ == '__main__':
    app.run()
