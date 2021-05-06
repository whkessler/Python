from flask import Flask
app = Flask(__name__)

@app.route('/')
def index ():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<name>')
def hi(name):
    return f'Hi {name}!'
@app.route('/repeat/<num>/<name>')
def repeat(num,name):
    result = name * int(num)
    return f"{result}"










if __name__=="__main__":
    app.run(debug=True)