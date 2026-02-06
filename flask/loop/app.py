from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    res_code=8
    return render_template('index.html', res_code=res_code)

@app.route('/loop')
def loop():
    l1 = ["1","2","3","4","5"]
    return render_template('loop.html', l1=l1)


if __name__=="__main__":
    app.run(debug=True)