#!/usr/bin/python3

from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)

