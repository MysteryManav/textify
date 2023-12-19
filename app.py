import os
import secrets
from forms import UploadPhoto
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from werkzeug.utils import secure_filename
from model import ocr_core

app = Flask(__name__)

# Bootstrap
Bootstrap(app)

# CSRF protection]
# app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
app.config["SECRET_KEY"] = "SECRET-TUNNEL"
app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")


@app.route("/", methods=["GET", "POST"])
def home_page():
    form = UploadPhoto()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        print(photo_path)
        photo.save(photo_path)
        text = ocr_core(photo_path)
        print(text)
        return render_template(
            "index.html", form=form, filename=filename, photo_path=photo_path, text=text
        )
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
