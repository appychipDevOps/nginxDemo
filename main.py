from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = "your Flask app"
    return f'Hello, World! This is app {message}'

if __name__ == '__main__':
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    app.run(host='0.0.0.0', port=port)
