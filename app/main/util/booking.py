from flask_restplus import Namespace, fields


class BookingDto:
    api = Namespace('Booking', description='booking related operations')
    bkg = api.model('Booking', {
    	'theatre':fields.String(required=True, description='theatre name'),
        'movie': fields.String(required=True, description='movie name'),
        'language': fields.String(required=True, description='langueage'),
        'seat_no': fields.String(required=True, description='seat no')
    })

