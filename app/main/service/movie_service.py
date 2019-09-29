import uuid
import datetime

from app.main import db
from app.main.model.movie import Movie

def save_new_movie(data):
    emp = Movie.query.filter_by(title=data['title']).first()
    if not emp:
        new_movie = Movie(
            public_id=str(uuid.uuid4()),
            title=data['title'],
            user_ratings=data['user_ratings'],
            cast=data['cast'],
            director=data['director'],
            duration_min=data['duration_min'],
            description=data['description'],
            price_movie=data['price'],
            released_on=data['datetime'],
            languages=data['languages']
        )
        save_changes(new_movie)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_movies():
    return Movie.query.all()


def get_a_movie(public_id):
    return Movie.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()