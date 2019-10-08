import uuid
import datetime

from app.main import db
from app.main.model.theatre import Theatre,Audi


def T_check(data):
    theatre = Theatre.query.filter_by(name=data['theatre']).first()
    if theatre:
    	A_check(data)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Theatre not found',
        }
        return response_object, 409

response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201

def A_check(data):
	audi=Audi.query.filter_by(name=data['audi']).first()
	if audi:
		S_check(data)
	else:
		response_object = {
            'status': 'fail',
            'message': 'audi not found',
        }
        return response_object, 409

def S_check(data):

	seat=Seat.query.filter_by(seat_no=data['seat']).first()
	





def get_all_movies():
    return Movie.query.all()


def get_a_movie(public_id):
    return Movie.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


