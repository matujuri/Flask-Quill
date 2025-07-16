from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_quill import Quill
from flask_quill.fields import QuillField
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
quill = Quill(app)
bootstrap5 = Bootstrap5(app)

class PostForm(FlaskForm):
    body = QuillField("Content", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        return f"Submitted content:<br><div style='border:1px solid #ccc;padding:1em'>{form.body.data}</div>"
    return render_template("form.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)