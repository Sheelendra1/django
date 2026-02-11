from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(200), nullable=False)
    password=db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        message = "User registered successfully!"
    return render_template('form.html', message=message)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        sno=request.form['sno']
        username=request.form['username']
        password=request.form['password']
        user = User.query.filter_by(sno=sno).first()

        if user:
            user.username = username
            user.password = password
            db.session.commit()
            return "User updated successfully!"
        else:
            return "User not found!"
    return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True)

