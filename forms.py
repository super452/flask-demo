from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from flask.ext.pagedown.fields import PageDownField

class LoginForm(Form):
	username = StringField('username', validators=[Required()])
	password = PasswordField('password', validators=[Required()])
	submit = SubmitField('log in')

class PostForm(Form):
	post = PageDownField("What's in your mind?", validators=[Required()])
	submit = SubmitField('submit')