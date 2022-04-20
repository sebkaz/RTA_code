
from flask import Flask
from flask import request

# Create a flask
app = Flask(__name__)

# Create an API end point
@app.route('/hello', methods=['GET'])
def say_hello():
    name = request.args.get("name", "")
    title = request.args.get("title", "")
    if name:
        resp = f"Hello {title} {name}" if title else f"Hello {name}"
    else:
        resp = f"Hello {title}" if title else "Hello"
    return resp

if __name__ == '__main__':
    app.run()
