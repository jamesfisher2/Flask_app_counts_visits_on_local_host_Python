from flask import Flask, redirect

#redirecting from http://127.0.0.1:5000 to desired link and counting such visits to the terminal
TARGET = 'https://openai.com/'

app = Flask(__name__)

counter = 0

@app.route("/")
def hello_world():
    global counter

    counter +=1
    print("counter = ", counter)
    return redirect(TARGET)

app.run(debug=True)