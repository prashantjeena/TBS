import uuid
import datetime

from app.main import db
from app.main.model.theatre import Theatre,Audi,Seat,Movie,Showing,Date,Slot,Reservation


def seat_checker(data):
	T_check(data)

def T_check(data):
    theatre = Theatre.query.filter_by(name=data['theatre']).first()
    if theatre:
    	A_check(data)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Theatre not found'
        }
        return response_object, 409

def A_check(data):
	audi=Audi.query.filter_by(name=data['audi']).first()
	if audi:
		S_check(data)
	else:
		response_object = {
            'status': 'fail',
            'message': 'Audi not found'
        }
		return response_object, 409
def S_check(data):

	seat=Seat.query.filter_by(seat_no=data['seat']).first()
	if seat.status=='available':
		response_object = {
            'status': 'success',
            'message': 'Seat is available'
        }
		return response_object, 201
	else:
		response_object = {
            'status': 'fail',
            'message': 'Seat is unavailable'
        }
		return response_object 

#def available_seats(data):
	#return Seat.query.filter(Audi.status==1).filter_by(audi_id=audi_id).filter()
	
def save_new_showing_details(data):
	show=Showing.query.filter_by(audi_id=data['audi_id']).filter_by(date_id=data['date_id']).filter_by(movie_id=data['movie_id']).filter_by(slot_id=data['slot_id']).first()
	if not show:
		new_show = Showing(
			public_id=str(uuid.uuid4()),
            slot_id=data['slot_id'],
            audi_id=data['audi_id'],
            date_id=data['date_id'],
            movie_id=data['movie_id'])
		save_changes(new_show)
		response_object = {
            'status': 'success',
            'message': 'show detail successfully saved ',
        }
		return response_object, 201
	else:
		response_object = {
			'status': 'fail',
			'message': 'show already exists.',
		}
		return response_object, 409

def get_audis_movie(title):
	return Audi.query.filter_by(title=title)

def get_all_movies():
    return Movie.query.all()

def get_a_movie(title):
	return Movie.query.filter_by(title=title).first()

def language_checker(name,language):
	if language.lower()=='hindi':
		movie=Movie.query.filter_by(Hindi=True).filter_by(name=name).first()
		if movie:
			return movie
		else:
			print('Movie not available in Hindi. Please select a different language')
			
	if language.lower()=='english':
		movie=Movie.query.filter_by(English=True).filter_by(name=name).first()
		if movie:
			return movie
		else:
			print('Movie not available in English. Please select a different language')

#def get_audi_list_for_a_movie(name):
 #   return movie_audi.query.with_entities(movie_audi.Audi_name).filter_by(name=Movie_name).first()

def get_all_movie_from_a_theatre(theatre_id):
	return Movie.query.filter_by(theatre_id=theatre_id).first()

##date functions

def save_a_date(data):
	date=Date.query.filter_by(date=data['date']).first()
	if not date:
		new_date=Date(
			date=data['date']
			)
		save_changes(new_date)
		response_object = {
            'status': 'success',
            'message': 'date detail successfully saved ',
        }
		return response_object, 201
	else:
		response_object = {
			'status': 'fail',
			'message': 'date already exists.',
		}
		return response_object, 409

def save_a_slot(data):
	slot=Slot.query.filter_by(slot_num=data['slot_num']).first()
	if not slot:
		new_slot=Slot(
			slot_num=data['slot_num'],
			time=data['time']
			)
		save_changes(new_slot)
		response_object = {
            'status': 'success',
            'message': 'slot detail successfully saved ',
        }
		return response_object, 201
	else:
		response_object = {
			'status': 'fail',
			'message': 'slot already exists.',
		}
		return response_object, 409

def save_a_reservation(data):
	rsrv=Reservation.query.filter_by(showing_id=data['showing_id']).first()
	if not rsrv:
		seat_id=Seat.query.with_entities(Seat.id).filter_by(audi_id=(Showing.query.with_entities(Showing.audi_id).filter_by(id=data['showing_id']).first())).all()
		seat_id=[id for id in seat_id]
		for i in seat_id:
			new_rsrv=Reservation(
				seat_id=i,
				showing_id=data['showing_id']
				)
			save_changes(new_rsrv)
		response_object = {
            'status': 'success',
            'message': 'Reservation detail successfully saved ',
        }
		return response_object, 201
	else:
		response_object = {
			'status': 'fail',
			'message': 'Reservation already exists.',
		}
		return response_object, 409


def save_changes(data):
    db.session.add(data)
    db.session.commit()



