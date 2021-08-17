from . import db

class User(db.Model):
    __tablename__ = 'users'

    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    profile_pic = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='users', lazy= 'dynamic')
    date_join = db.Column(db.DateTime, default = datetime.utcnow())