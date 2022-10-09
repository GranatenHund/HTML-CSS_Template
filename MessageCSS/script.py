from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/')
def message():
    return render_template('message.html') 


if __name__ == "__main__":
    app.run(debug = True)	