from flask_restplus import Namespace, fields


class TheatreDto:
    api = Namespace('Theatre', description='Theatre related operations')
    thtr = api.model('Theatre_details', {
        'id':fields.Integer(description='theatre id'),
    	'name':fields.String(required=True, description='theatre name'),  
        'description': fields.String(description='description of auditorium'),
        'base_price': fields.Integer(required=True,description='base price of a theatre'),
        'public_id': fields.String(description='theatre Identifier')
    })

class AudiDto:
    api = Namespace('Audi', description='Audi related operations')
    audi = api.model('Audi_details', {
        'id':fields.Integer(description='audi id'),
        'audi_name': fields.String(required=True, description='name of auditorium '),
        'rows': fields.Integer(required=True, description='rows in audi '),
        'columns': fields.Integer(required=True, description='columns in audi '),
        'theatre_id': fields.Integer(required=True, description='theatre id of audi '),
        'public_id': fields.String(description='audi Identifier')
    })

class SeatDto:
    api = Namespace('Seat', description='Seat related operations')
    seat = api.model('Seat_details', {
        'rows': fields.Integer(required=True, description='rows in audi '),
        'columns': fields.Integer(required=True, description='columns in audi '),
        'audi_id': fields.Integer(required=True, description='audi id of seat '),
        'status' : fields.String(required=True,description='availability of a seat'),
        'public_id': fields.String(description='seat Identifier')
    })


