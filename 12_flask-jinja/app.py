# Stanley Hoo, Tahmim Hassan, Leon Huang
# UWSD
# SoftDev
# K12 -- Just plug it in
# 2024-09-26
# time spent: 0.5

"""
NOTES:
in the my foist template webpage it shows the array in numbers and new lines

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
<your response here>
Prediction: return render_template will give an error
Actual: Says render_template is not defined

Q1:
<your response here>
http://127.0.0.1:5000/my_foist_template

Q2:
<your response here>
'model_tmplt.html' --> html page to load
foo, collection --> data we pass to the html web page through this python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


img = os.path.join('static', 'Image')
 #run this code with url: http://127.0.0.1:5000/ILOVEMYKOLYK for results!
@app.route("/ILOVEMYKOLYK")
def home():
    file = os.path.join(img, 'startrek.jpg')
    return render_template('mykolyk.html', image=file)
 

if __name__ == "__main__":
    app.debug = True
    app.run()
