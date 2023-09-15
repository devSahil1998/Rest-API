from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/square/<int:n>')    
def square(n):
  copy_n = n
  x = copy_n*copy_n
  y = copy_n*copy_n*copy_n
  result = {
    "Number" : copy_n,
    "Square" : x,
    "Cube" : y,
    "Author" : "Sahil"
  }
  return jsonify(result)
     

if __name__ == "__main__":
    app.run(debug = True)
