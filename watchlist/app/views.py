from flask import render_template
from app import app
from .request import get_movies
from .requests import get_movies,get_movie,search_movie
#views
@app.route('/movie/<int:id>')
def movie(id):


    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)