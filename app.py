from flask import Flask,render_template, request,redirect,url_for
app=Flask(__name__)

data={}

@app.route('/',methods=["POST","GET"])
def index():
    if request.method=='POST':
        nam=request.form['name']
        email=request.form['email']
        phone=request.form['Phone']
        team=request.form['team']
        feedback=request.form['feedback']
        data['name']=nam
        data['email']=email
        data['Phone']=phone
        data['team']=team
        data['feedback']=feedback
        return redirect(url_for('input'))
    else:
        return render_template('index.html')



@app.route('/input')
def input():
    return render_template('input.html',nm=data['name'],
    em=data['email'],
    ph=data['Phone'],
    tm=data['team'],
    fb=data['feedback'])


if __name__== '__main__':
    app.run