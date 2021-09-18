# from flask import render_template, redirect, url_for
# from . import main
# from .forms import ReviewForm

# # Views
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     message = 'Moses Kinyua Mugo'
#     title = 'Home - welcome to the Best Movie Reviews Website Online'

#     return render_template('index.html', message = message, title = title)


# @main.route('/movie/<int:movie_id>')
# def movie(movie_id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     return render_template('movie.html')