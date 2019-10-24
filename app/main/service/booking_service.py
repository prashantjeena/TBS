import uuid
import datetime

from ..service.blacklist_service import save_token
from app.main import db
from app.main.model.theatre import Theatre,Audi,Seat,Movie,Showing,Date,Slot,Reservation

def seat_list(movie_id,date_id,slot_id):
    audi=Slot.query.with_entities(audi_id).filter_by(slot_id=id).one()
    show=Showing.query.with_entities(id).filter_by(slot_id=slot_id).filter_by(movie_id=movie_id).filter_by(date_id=date_id).filter_by(audi_id=audi).one()
    seat=Reservation.query.with_entities(seat_id).filter_by(status=True).filter_by(showing_id=show).all()
    seat_list=Seat.query.with_entities(seat_no).filter_by(id=seat).all()
    return seat_list

def showtime(movie_id,date_id):
    show_time=Slot.query.with_entities(time).filter_by(id=(Showing.query.with_entities(slot_id).filter_by(movie_id=movie_id).filter_by(date_id=date_id).all())).all()
    return show_time

def book_a_ticket(data):
    try:
        # fetch the reservation data
        rsrv=Reservation.query.filter_by(showing_id=data['showing_id']).filter_by(seat_id=(Seat.query.with_entities(Seat.id).filter_by(seat_no=data['seat_no']).first())).first()
        if rsrv.status==True:
            edit_details(data)
            auth_token = rsrv.encode_auth_token(rsrv.id)
            if auth_token:
                response_object = {
                    'status': 'success',
                    'message': 'Seat successfully reserved ',
                    'Authorization': auth_token.decode()
                }
                return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'This seat is taken. Please select a different seat'
            }
            return response_object, 401

    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Try again'
        }
        return response_object, 500

def get_all_movies():
    return Movie.query.all()

def get_a_movie(title):
    return Movie.query.filter_by(title=title).first()

def get_all_movies_from_theatre(theatre_id):
    return Movie.query.filter_by(theatre_id=theatre_id).all()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def edit_details(data):
    Reservation.query.filter_by(showing_id=data['showing_id']).update(dict(status=False))
    db.session.commit()

