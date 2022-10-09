from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/table/<int:num>')
def table(num):
   return render_template('print_table.html',n = num)


           


if __name__ == "__main__":
    app.run(debug = True)	