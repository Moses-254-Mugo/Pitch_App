from flask import render_template,request, redirect, url_for,abort
from . import main
from .forms import ReviewForm
from flask_login import login_required
from ..models import Reviews, User

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Moses Kinyua Mugo'
    title = 'Home - welcome to the Best Movie Reviews Website Online'

    return render_template('index.html', message = message, title = title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)