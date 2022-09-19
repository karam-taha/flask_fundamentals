from ast import Num
from flask import Flask
app= Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    print(name)
    return 'Hi' + ' ' + name +'!'

@app.route('/repeat/<num>/<name>')
def rep(num,name):
    newName=""
    for x in range(int(num)):
        newName+=name+" "
    print(newName)
    return newName

if __name__=="__main__":
    app.run(debug=True)