from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from . import main
from .forms import UpdateProfile
from .. import db
from ..models import User

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home'
    
    return render_template('index.html', title = title)


# @main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
# @login_required
# def comment(pitch_id):
#     form = CommentForm()
#     pitch = Pitch.query.get(pitch_id)
#     all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
#     if form.validate_on_submit():
#         comment = form.comment.data 
#         pitch_id = pitch_id
#         user_id = current_user._get_current_object().id
#         new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
#         new_comment.save_c()
#         return redirect(url_for('.comment', pitch_id = pitch_id))
#     return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)