from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/industry'
db=SQLAlchemy(app)

class employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_Name=db.Column(db.Text,default="First-name",unique=False)
    Last_Name=db.Column(db.Text,default="First-name",unique=False)
    Password=db.Column(db.Text,default="Password",unique=False)
    Phone_Number=db.Column(db.Integer,default="Something",unique=False)

@app.route('/')
def main():
    all_data = employee.query.all()
    return render_template('main.html',data=all_data)

@app.route('/sign',methods=['GET','POST'])
def sign():
    if (request.method=='POST'):
        first=request.form.get('firstname')
        last=request.form.get('lastname')
        password=request.form.get('password')
        phn=request.form.get('phnno')
        entry=employee(First_Name = first,Last_Name=last,Password=password,Phone_Number=phn)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('main'))
    else:
        return render_template('sign-up.html')
@app.route('/update')
def update():
    return render_template('update.html')

if __name__=='__main__':
    app.run(debug=True)