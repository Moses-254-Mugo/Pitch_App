from flask import render_template,request, redirect, url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile
from flask_login import login_required,current_user
from ..models import User, Pitch, Comment
from .. import db,photos
import markdown2
from .forms import ReviewForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Welcome to Pitch App'

    love_pitches  = Pitch.get_pitches('love')
    motivational_pitches = Pitch.get_pitches('motivational')


    return render_template('index.html',title= title, love =love_pitches, motivational = motivational_pitches)


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

@main.route('/pitches/love_pitches',methods = ['GET','POST'])
def love_pitches():
    pitches =  Pitch.get_pitches('love')
    
    Review_Form = ReviewForm()
    return render_template('love_pitch.html',pitches = pitches, Review_Form = Review_Form )



@main.route('/motivational_pitch',methods = ['GET','POST'])
def motivational_pitches():
    pitches =  Pitch.get_pitches('motivational')
    Review_Form = ReviewForm()

    return render_template('motivational_pitch.html',pitches = pitches, Review_Form = Review_Form  )


@main.route('/pitch/<int:id>', methods = ['GET','POST'])
@login_required
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.posted_date.strftime('%b %d, %Y')
    
    if request.args.get("like"):
        pitch.like = pitch.like + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{p_id}".format(p_id=pitch.id))

    elif request.args.get("downvote"):
        pitch.dislike = pitch.dislike + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{p_id}".format(p_id=pitch.id))
