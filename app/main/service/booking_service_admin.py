import uuid
import datetime

from app.main import db
from app.main.model.theatre import Theatre,Audi,Seat,Movie,Showing,Date,Slot,Reservation


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

def language_checker(title,language):
	if language.lower()=='hindi':
		if Movie.query.filter_by(Hindi=True).filter_by(title=title).first():
			return 'available in hindi'
	if language.lower()=='english':
		if Movie.query.filter_by(English=True).filter_by(title=title).first():
			return 'available in english'

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
			time=data['time'],
			audi_id=data['audi_id']
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
				status=data['status'],
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



