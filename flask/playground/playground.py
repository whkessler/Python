from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<x>')
def playx(x):
    repeat = int(x)
    return render_template("index1.html", repeat=repeat)

@app.route('/play/<x>/<color>')
def playcolor(x,color):
    repeat = int(x)
    color = color
    return  render_template("index2.html", color=color, repeat=repeat)









if __name__ == "__main__":
    app.run(debug = True)