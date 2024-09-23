# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>
Importing Python libs through pip
activating virtual machine through using virtual machine /bin/activate

QCC:
0. Initializing a file in Java, or an object like 'Card uno = Card(name)'
1. The point of reference for '/' in terminal is your main directory
2. In the terminal
3. I think it will print the name of the directory the app is routed to
4. It appears in a httml link, we know because when we run it gives us a link.
5. Running a function defined in an object like a static or non static function.
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 We recognized initializing and calling functions of objects from APCS
 and then ran the code to see that there was a "running on __link__" that sent us to a
 webpage that said 'No hablo queso!'
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?
