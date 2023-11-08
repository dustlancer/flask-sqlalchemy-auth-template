from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Note, User, Like
from . import db

main = Blueprint('main', __name__)



@main.route('/like', methods=['POST'])
def like_note_post():
    data = request.json
    print(data.get("note_id"))
    existing_like = Like.query.filter_by(user_id = current_user.id, note_id=data.get("note_id")).first()

    if existing_like == None:
        new_like = Like(user_id = current_user.id, note_id = data.get("note_id"))
        db.session.add(new_like)
        db.session.commit()
        return jsonify({"msg":"like_set"})
    
    else: 
        db.session.delete(existing_like)
        db.session.commit()
        return jsonify({"msg":"like_removed"})
        

        

    print(existing_like)
    return "ok"


@main.route("/get_likes_count/<_id>")
def get_likes_amount(_id):
    count = int(Like.query.filter_by(note_id=_id).count())
    print("respinsed ", count)
    return {"count": count}



@main.route('/')
def index():
    notes = Note.query.all()
    notes.reverse()

    return render_template('index.html', notes=notes)



@main.route('/profile', methods=['POST'])
@login_required
def profile_post():
    title = request.form.get('title')
    text = request.form.get('text')
    new_note = Note(title=title, text=text, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    print("Note added")
    return redirect(url_for('main.profile'))


@main.route('/profile')
@login_required
def profile():
    user_notes = Note.query.filter_by(user_id=current_user.id).all()
    user_notes.reverse()
    return render_template('profile.html', name=current_user.name, user_notes=user_notes)


