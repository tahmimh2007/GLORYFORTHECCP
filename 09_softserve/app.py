# Ivan Gontchar
# Fire Marshalls(Jason Chao, Tahmim Hassan)
# SoftDev
# K09 -- Putting it Together
# 2024-09-24
# time spent: 1 hour

from flask import Flask
import numbercruncher

app = Flask(__name__)

@app.route("/")                 #assign fxn to route
def hello_world():
    print(__name__)
    return '''<h3>
    Ivan Gontchar<br>
    Fire Marshalls<br>
    SoftDev<br>
    K09 -- Putting it Together<br>
    2024-09-24<br>
    time spent: 1 hour</h3><br><br><b>''' + numbercruncher.maker()

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
