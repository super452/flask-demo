from app import app
from app import db


app.config['SQLALCHEMY_DATABASE_URI'] =\
'mysql+pymysql://username:password/@localhost/db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	password = db.Column(db.String(64))
	posts = db.relationship('Post', backref='user')

	def __repr__(self):
		return '<User %r>' %self.name


class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	post = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return '<User %r>' %self.name


