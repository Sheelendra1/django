from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/feedback', methods=['POST','GET'])
def feedback():
    error = None

    if request.method == 'POST':
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')

        if not name or not email or not message:
            error="all are required"
        elif '@' not in email:
            error="Enter valid email"
        else:
            print(name,email,message)
            return render_template('thankyou.html', name=name)
    return render_template('feedback.html',error=error)

if __name__ == '__main__':
    app.run(debug=True)
