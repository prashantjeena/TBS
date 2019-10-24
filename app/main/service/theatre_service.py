import uuid
import datetime

from app.main import db
from app.main.model.theatre import Theatre,Audi,Seat,Movie

def save_new_theatre(data):
    theatre = Theatre.query.filter_by(name=data['name']).first()
    if not theatre:  
        new_theatre = Theatre(
            public_id=str(uuid.uuid4()),
            name=data['name'],
            description=data['description'],
            base_price=data['base_price']    
        )
        save_changes(new_theatre)
        response_object = {
            'status': 'success',
            'message': 'theatre successfully saved ',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'theatre already exists.',
        }
        return response_object, 409

def get_all_theatres():
    return Theatre.query.all()


def get_a_theatre(public_id):
    return Theatre.query.filter_by(public_id=public_id).first()

def save_new_audi(data):
    audi = Audi.query.filter_by(audi_name=data['audi_name']).first()
    if not audi:  
        new_audi = Audi(
            public_id=str(uuid.uuid4()),
            audi_name=data['audi_name'],
            rows=data['rows'],
            columns=data['columns'],
            theatre_id=data['theatre_id']
        )
        save_changes(new_audi)
        response_object = {
            'status': 'success',
            'message': 'audi successfully saved ',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'audi already exists.',
        }
        return response_object, 409

def get_all_audi():
    return Audi.query.all()

def get_audi_theatre(theatre_id):
    return Audi.query.filter_by(theatre_id=theatre_id).all()

def get_an_audi(public_id):
    return Audi.query.filter_by(public_id=public_id).first()	   


def init_seats_in_audi(data):
    r=Audi.query.with_entities(Audi.rows).filter(Audi.id==data['audi_id']).scalar()
    c=Audi.query.with_entities(Audi.rows).filter(Audi.id==data['audi_id']).scalar()
    for i in range(1,r+1):
        for j in range(1,c+1):
            if i < r+1 and i > r-2:
                seat=Seat(public_id=str(uuid.uuid4()),
                seat_no=str(i)+str(j),
                audi_id=data['audi_id'],
                seat_type='platinum',
                seat_price=100
                )
                save_changes(seat)
            elif i < r-1 and i > r-4 :
                seat=Seat(public_id=str(uuid.uuid4()),
                seat_no=str(i)+str(j),
                audi_id=data['audi_id'],
                seat_type='gold',
                seat_price=50
                )
                save_changes(seat)
            elif i<r-3:
                seat=Seat(public_id=str(uuid.uuid4()),
                seat_no=str(i)+str(j),
                audi_id=data['audi_id']
                )
            save_changes(seat)




def get_all_seats():
    return Seat.query.all()


def get_a_seat(public_id):
    return Seat.query.filter_by(public_id=public_id).first()

def save_new_movie(data):
    mov = Movie.query.filter_by(title=data['title']).first()
    if not mov:
        if 'hindi' in data['language'].lower():
            h=True
        else:
            h=False

        if 'english' in data['language'].lower():
            e=True
        else:
            e=False

        new_movie = Movie(
            title=data['title'],
            public_id=str(uuid.uuid4()),
            cast=data['cast'],
            director=data['director'],
            duration_min=data['duration_min'],
            description=data['description'],
            released_on=data['released_on'],
            theatre_id=data['theatre_id'],
            Hindi=h,
            English=e
            
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
            'message': 'movie already exists. Please save a new one.',
        }
        return response_object, 409


def get_all_movies():
    return Movie.query.all()

def get_a_movie(public_id):
    return Movie.query.filter_by(public_id=public_id).first()

def get_a_movie_hindi(name):
    return Movie.query.filter_by(name=title).filter_by(Hindi=True).first()

def get_a_movie_english(name):
    return Movie.query.filter_by(name=title).filter_by(English=True).first()

def save_changes(data):

	db.session.add(data)
	db.session.commit()


