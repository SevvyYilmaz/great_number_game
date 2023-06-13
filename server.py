from flask import Flask, render_template,request, redirect, session
import random
app = Flask(__name__)
app.secret_key="Shhh, This is a secret" # in order for session to work we need a key 

@app.route('/')
def homepage(): 
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1,100)
    return render_template('homepage.html')


@app.route('/guess', methods = ['POST'])
def guess_the_number():
    session['guessed_number'] = int(request.form['number'])
    # this assign the number from user to a variable called guessed number
    #need to type cast the request form or HTML 
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

