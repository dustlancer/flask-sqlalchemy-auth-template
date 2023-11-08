from . import db

from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="notes")

    def get_username(self):
        return self.user.name


    def get_likes(self):
        return Like.query.filter_by(note_id=self.id).count()

    def is_liked_by_user(self, _user_id):
        like = Like.query.filter_by(user_id = _user_id, note_id=self.id).first()
        if like:
            return True
        else:
            return False




class Like(db.Model):
    __tablename__ = 'like'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    note_id = db.Column(db.Integer, db.ForeignKey("note.id"))
    user = db.relationship("User", backref="likes")
    note = db.relationship("Note", backref="likes")