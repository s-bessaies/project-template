from flask import Flask

app = Flask(__name__)

@app.route('/api1', methods=['GET'])
def api1():
    return "call api1"

@app.route('/sayhello', methods=['GET'])
def sayhello():
    return "Hello"

if __name__ == '__main__':
    app.run(port=4000)