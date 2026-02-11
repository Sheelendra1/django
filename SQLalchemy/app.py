from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from flask_sqlalchemy import SQLAlchemy
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

with app.app_context():
    db.create_all()

# ---------- UPLOAD IMAGE ----------
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files.get('image')

        if not file or file.filename == '':
            flash("No file selected")
            return redirect('/')

        image = Image(
            filename=file.filename,
            data=file.read()   # convert image to bytes
        )

        db.session.add(image)
        db.session.commit()

        flash("Image stored in database successfully")
        return redirect('/')

    images = Image.query.all()
    return render_template('upload.html', images=images)

# ---------- DISPLAY IMAGE ----------
@app.route('/image/<int:image_id>')
def get_image(image_id):
    image = Image.query.get_or_404(image_id)
    return send_file(
        io.BytesIO(image.data),
        mimetype='image/jpeg'
    )

if __name__ == '__main__':
    app.run(debug=True)
