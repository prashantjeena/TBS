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
        'audi_id': fields.Integer(required=True, description='audi id of seat '),
        'status' : fields.String(required=True,description='availability of a seat'),
        'seat' : fields.String(required=True,description='seat number'),
        'public_id': fields.String(description='seat Identifier')
    })

class MovieDto:
    api = Namespace('movie', description='Movie related operations')
    mov = api.model('movie', {
        'title':fields.String(required=True, description='movie title'),
        'cast': fields.String( description='cast of the movie'),
        'director': fields.String( description='director of the movie'),
        'duration_min':fields.Integer( description='duration of the movie'),
        'description': fields.String( description='description of the movie'),
        'public_id': fields.String(description='Movie Identifier'),
        'released_on': fields.DateTime(description='release date and time'),      
        'language':fields.String(description='language the movie is available in'),
        'theatre_id':fields.Integer(description='theatre identifier of movie')

    })

class ShowingDto:
    api = Namespace('Showing', description='Showing related operations')
    show = api.model('show_details', {
        'id':fields.Integer(description='show id'),
        'slot_id': fields.Integer(required=True, description='slot id of show'),
        'movie_id': fields.Integer(required=True, description='movie id of show'),
        'date_id': fields.Integer(required=True, description='date id of show'),
        'audi_id': fields.Integer(required=True, description='audi id of show')
    })


class DateDto:
    api = Namespace('Date', description='Date related operations')
    dt = api.model('Dates', {
        'id':fields.Integer(description='Date id'),
        'date': fields.DateTime(description='date')
        })

class SlotDto:
    api = Namespace('Slot', description='Slots of an audi')
    slot = api.model('slot_details', {
        'id':fields.Integer(description='slot id'),
        'slot_num': fields.Integer(required=True, description='slot Identifier'),
        'time': fields.DateTime(required=True, description='time of the slot'),
        'audi_id': fields.Integer(required=True, description='audi id of the slot')
    })

class ReservationDto:
    api = Namespace('Reservation', description='Reservation related operations')
    rsrv = api.model('Reservation_details', {
        'id':fields.Integer(description='Reservation id'),
        'status':fields.Boolean(description='status of availability'),
        'showing_id': fields.Integer(required=True, description='showing id of Reservation')
    })



