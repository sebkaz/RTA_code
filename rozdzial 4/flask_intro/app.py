
from flask import Flask

# Create a flask
app = Flask(__name__)

# Create an API end point
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
