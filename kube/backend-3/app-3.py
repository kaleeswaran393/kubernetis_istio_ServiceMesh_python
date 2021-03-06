from flask import Flask, jsonify,request
import socket
import requests

app = Flask(__name__)


@app.route('/hit-backend', methods=['POST'])
def backend3():
    content = request.get_json()
    content["target"] = "backend-3"
    content["podIp"] = socket.gethostbyname(socket.gethostname())
    print(content)
    return str(content);

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)