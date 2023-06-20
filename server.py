from flask import Flask, render_template, session, redirect,request
import random

app = Flask(__name__)

app.secret_key="ugh as if"

@app.route('/')                                     #localhost:5009/ 
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)            #create random number 

    return render_template("index.html")

@app.route('/guess',methods=['POST'])                        #processing the guess
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/new')                                        #localhost:5009/new  
def new():                                                      # clears session, redirect to '/' to start a new game
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5009)