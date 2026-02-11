from flask import Flask, render_template, redirect, session, request, flash
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.LargeBinary)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('email')
        image_file = request.files.get('image')

        if not username:
            flash("Username required")
            return redirect('/')

        if User.query.filter_by(username=username).first():
            flash("User already exists")
            return redirect('/')

        image_data = image_file.read() if image_file else None

        user = User(username=username, image=image_data)
        db.session.add(user)
        db.session.commit()

        flash("User saved successfully")
        return redirect('/')

    return render_template('index.html')

@app.route('/database')
def database():
    users = User.query.all()

    result = []
    for u in users:
        result.append({
            "id": u.id,
            "username": u.username,
            "image": base64.b64encode(u.image).decode('utf-8') if u.image else None
        })

    return render_template('database.html', users=result)

if __name__ == "__main__":
    app.run(debug=True)
