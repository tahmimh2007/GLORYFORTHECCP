# Tahmim Hassan, Jady Lei, Brian Liu
# Team: 45
# SoftDev Pd 4
# Sep 30 2024 

"""
QCC/DISCO:
 - in notes
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

# ~~ working code 
import csv
import random

with open("data/occupations.csv", newline="") as csvfile:
    #creates a dictionary for every row that can be parsed through
    reader = csv.DictReader(csvfile)
    jobs = []
    percents = []
    full = []
    for row in reader:
        jobs.append(row['Job Class']), percents.append(float(row['Percentage']))
        full.append({"Job Class": row['Job Class'], "Percentage": row['Percentage'], "Link": row["Link"]})

def ReturnRandom():
# random.choices returns a list, [:-1] to ignore last row, k is returned list size
    return (random.choices(jobs[:-1], weights=percents[:-1], k=1)[0])

# ~~ back to app stuff

@app.route("/wdywtbwygp") 
def test_tmplt():
    return render_template( 'tablified.html', foo= ReturnRandom(), coll = full)

if __name__ == "__main__":
    app.debug = True
    app.run()
