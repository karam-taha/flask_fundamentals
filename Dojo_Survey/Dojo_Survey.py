from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    # if request.method == 'POST':
    #     print(request.form.get('people'))
    return render_template("index.html")

@app.route('/users', methods=['GET','POST','PUT'])
def create_user():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    session['check']=request.form['check']
    return redirect("/result")
    
@app.route("/result")
def show_user():
    return render_template("result.html",name=session['name'],location=session['location'],
    language=session['language'],comment=session['comment'],check=['check'])

if __name__ == "__main__":
    app.run(debug=True)