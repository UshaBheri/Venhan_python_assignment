from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    message = {"message": f"Hello, {name}!"}
    return jsonify(message)
