from flask import Flask

app = Flask(__name__)
IP = '0.0.0.0'
PORT = 3333

@app.route('/')
def hello():
    return "Hi!"

if __name__== '__main__':
    app.run(IP, port=PORT, debug=True)
