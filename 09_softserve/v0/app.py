# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # initializing a Flask

@app.route("/")                # routing it to directory
def hello_world():
    print(__name__)            # print name of module "__main__"
    return "No hablo queso!"   # prints out "No hablo queso!"

app.run()                      # runs the app
