from flask import render_template,redirect,url_for,flash,request
from flask_login import login_required,current_user
from . import main
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos
from ..models import User,Pitch,Comment,Upvote,Downvote
# import markdown2 

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home'
    
    return render_template('index.html', title = title)


@main.route('/about')
def about():

    '''
    View root page function that returns the about page and its data
    '''
    
    title = 'About Us'
    
    return render_template('about.html', title = title)


@main.route('/pitches/<category>')
@login_required
def category(category):
    pitch = Pitch.query.filter_by(category=category).all()
    print(pitch)
    return render_template('category.html', pitch = pitch)


@main.route('/comments/<id>')
@login_required
def comments(comments):
    comment = Comment.query.filter_by(id=id).all()
    print(pitch)
    
    return render_template('category.html', pitch = pitch)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    print(current_user)
    pitches = Pitch.query.filter_by(user_id=user_id).all()
    print(pitches)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, pitches = pitches)


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


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/create_pitch',methods = ['GET','POST'])
@login_required
def create_pitch():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'create_pitch'
    form = PitchForm()
    print(form.errors)
    if form.is_submitted():
        print('submitted')
    if form.validate():
        print("valid")
    print(form.errors)
    if form.validate_on_submit():
        title = form.title.data
        user_id = current_user._get_current_object().id
        content = form.content.data
        category = form.category.data
        new_pitch = Pitch(title = title,content=content,user_id = user_id,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for("main.category",category = category))
    
    return render_template('create_pitch.html', title = title, form = form)


@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        
        return redirect(url_for('.comment', pitch_id = pitch_id))
    
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)


@main.route('/upvote/<int:id>',methods = ['POST','GET'])
@login_required
def upvote(id):
    pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))


@main.route('/downvote/<int:id>',methods = ['POST','GET'])
@login_required
def downvote(id):
    pitches = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))