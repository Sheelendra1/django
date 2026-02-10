from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to home"

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')

        return f"welcome {username} | your email {email}"
    
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)