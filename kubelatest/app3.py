from flask import Flask, jsonify,request
import socket

app = Flask(__name__)

@app.route('/hit_backend', methods=['POST'])
def backend():
    content = request.get_json()
    content["service_name"] = content["target"]
    del content['target']
    content["podIp"] = socket.gethostbyname(socket.gethostname())
    return str(content);


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)