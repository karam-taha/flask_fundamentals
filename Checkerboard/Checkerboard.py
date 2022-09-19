from flask import Flask, render_template

app= Flask(__name__)
@app.route('/')
def checkboard():
    return render_template("index.html")

@app.route('/<int:y>')
def checkboard2(y):
    return render_template("index2.html",y=int(y))

@app.route('/<int:x>/<int:y>')
def checkboard3(x,y):
    return render_template("index3.html",x=int(x),y=int(y))

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkboard4(x,y,color1,color2):
    return render_template("index4.html",x=int(x),y=int(y),color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)