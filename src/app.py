# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, render_template_string, Markup
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
from jinja2 import escape

app = Flask(__name__)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.secret_key = 'secret string'

ckeditor = CKEditor(app)


class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        if 'flag' in form.title.data.lower() or 'flag' in form.title.data.lower():
            flash("Why you miss your Flag?")
            return render_template('index.html', form=form)
        else:
            title = form.title.data
            body = form.body.data
            code = '''
	<div class="warpper" style="width: 700px; margin: auto">
		<h1> {{ title }} </h1>
		<hr>
		<p> %s </p>
		<hr>
		<a href="/">Home</a>
	</div>''' 
            html = code % (body)
            return render_template_string(html, title=title)
    return render_template('index.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(400)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run()
