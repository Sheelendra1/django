from flask import Flask, render_template, request,session,redirect,url_for

app=Flask(__name__)
app.secret_key = "secret123" 

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        
        return render_template('home.html')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    return render_template('index.html')
    