from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref='blogs')

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('home.html', blogs=blogs)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        pwd = bcrypt.generate_password_hash(request.form['password']).decode()
        user = User(username=request.form['username'], password=pwd)
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully")
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            return redirect('/')
        flash("Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/create', methods=['GET','POST'])
def create():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        blog = Blog(
            title=request.form['title'],
            content=request.form['content'],
            user_id=session['user_id']
        )
        db.session.add(blog)
        db.session.commit()
        return redirect('/')
    return render_template('create_blog.html')

@app.route('/blog/<int:id>')
def blog_detail(id):
    blog = Blog.query.get_or_404(id)
    return render_template('blog_detail.html', blog=blog)

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    blog = Blog.query.get_or_404(id)
    if blog.user_id != session.get('user_id'):
        return redirect('/')

    if request.method == 'POST':
        blog.title = request.form['title']
        blog.content = request.form['content']
        db.session.commit()
        return redirect(f'/blog/{id}')
    return render_template('edit_blog.html', blog=blog)

@app.route('/delete/<int:id>')
def delete(id):
    blog = Blog.query.get_or_404(id)
    if blog.user_id == session.get('user_id'):
        db.session.delete(blog)
        db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
