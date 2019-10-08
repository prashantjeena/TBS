import uuid
import datetime

from app.main import db
from app.main.model.theatre import Theatre,Audi,Seat


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
    return Audi.query.filter_by(theatre_id=theatre_id).first()

def get_an_audi(public_id):
    return Audi.query.filter_by(public_id=public_id).first()	   

def init_seats(data):
    for i in range(1,data['rows']):
    	for j in range(1,data['columns']):
    		if i < 7:
	    		seat=Seat(public_id=str(uuid.uuid4()),
	    			row=i,
	    			column=j,
	    			audi_id=data['audi_id']
	    			)
	    		save_changes(seat)
	    	elif i > 6 and i < 9 :
	    		seat=Seat(public_id=str(uuid.uuid4()),
					row=i,
					column=j,
					audi_id=data['audi_id'],
					seat_type='gold'
					)
	    		save_changes(seat)
	    	elif i>8:
	        	seat=Seat(public_id=str(uuid.uuid4()),
	        		row=i,
	        		column=j,
	        		audi_id=data['audi_id'],
	        		seat_type='platinum'
	        		)
	        	save_changes(seat)

def get_all_seats():
    return Seat.query.all()


def get_a_seat(public_id):
    return Seat.query.filter_by(public_id=public_id).first()

def seat_price(seat_no,bpi):

	if seat_type=='silver':
		seat_price=bpi
	elif seat_type=='gold' :
		seat_price=bpi+50
	elif seat_type=='platinum':
		seat_price=bpi+100
	return seat_price 

def save_changes(data):

	db.session.add(data)
	db.session.commit()


