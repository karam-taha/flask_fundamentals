from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    session['check1']=request.form['check1']
    return redirect("/result")
    
@app.route("/result")
def show_user():
    return render_template("result.html",name=session['name'],location=session['location'],
    language=session['language'],comment=session['comment'],check=['check1'])

if __name__ == "__main__":
    app.run(debug=True)