from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")

        if '@' not in email:
            error = "please enter valid email"
            return render_template("register.html", error=error)
        
        elif name and email and course:
            students.append({"name": name, "email": email, "course": course})
            return redirect(url_for("students_page"))
            
    return render_template("register.html",error=error)

@app.route("/students")
def students_page():
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
