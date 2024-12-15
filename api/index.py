from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    url = "https://www.sandollcloud.com/webapi/search/recognitionupload"
    headers = {"accept": "application/json", "x-requested-with": "XMLHttpRequest"}
    
    if 'image_file' not in request.files:
        return jsonify({'error': '이미지 파일이 없습니다.'}), 400
        
    image_file = request.files['image_file']
    
    response = requests.post(
        url, 
        headers=headers, 
        files={'image_file': (image_file.filename, image_file.read())}
    )
    return jsonify(response.json())

@app.route('/recognition', methods=['POST'])
def recognition():
    url = "https://www.sandollcloud.com/webapi/search/recognitionfonts"
    headers = {"accept": "application/json", "content-type": "application/json"}
    result = requests.post(url, headers=headers, json=request.json).json()
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)