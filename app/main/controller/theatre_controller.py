from flask import request
from flask_restplus import Resource

from ..util.theatre_util import TheatreDto,AudiDto,SeatDto
from ..service.theatre_service import save_new_theatre, get_all_theatres, get_a_theatre
from ..service.theatre_service import save_new_audi, get_all_audi, get_an_audi
from ..service.theatre_service import init_seats

api = TheatreDto.api
_thtr = TheatreDto.thtr

bpi= AudiDto.api
_audi=AudiDto.audi

spi= SeatDto.api
_seat=SeatDto.seat



@api.route('/')
class TheatreList(Resource):
    @api.doc('list_of_registered_theatres')
    @api.marshal_list_with(_thtr, envelope='data')
    def get(self):
        """List all registered theatres"""
        return get_all_theatres()

    @api.response(201, 'Theatre successfully created.')
    @api.doc('create a new theatre')
    @api.expect(_thtr, validate=True)
    def post(self):
        """Creates a new theatre """
        data = request.json
        return save_new_theatre(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The theatre identifier')
@api.response(404, 'Employee not found.')
class Theatre(Resource):
    @api.doc('get a theatre')
    @api.marshal_with(_thtr)
    def get(self, public_id):
        """get a theatre given its identifier"""
        theatre = get_a_theatre(public_id)
        if not theatre:
            api.abort(404)
        else:
            return theatre

@bpi.route('/')
class AudiList(Resource):
    @bpi.doc('list_of_registered_auditoriums')
    @bpi.marshal_list_with(_audi, envelope='data')
    def get(self):
        """List all registered auditoriums"""
        return get_all_audi()

    @bpi.response(201, 'Auditorium successfully created.')
    @bpi.doc('create a new Audi')
    @bpi.expect(_audi, validate=True)
    def post(self):
        """Creates a new Audi """
        data = request.json
        return save_new_audi(data=data)


@bpi.route('/<public_id>')
@bpi.param('public_id', 'The audi identifier')
@bpi.response(404, 'audi not found.')

class Audi(Resource):
    @bpi.doc('get an Audi')
    @bpi.marshal_with(_audi)
    def get(self, public_id):
        """get an audi given its identifier"""
        audi = get_an_audi(public_id)
        if not audi:
            api.abort(404)
        else:
            return audi

@spi.route('/')
class SeatMap(Resource):
    @spi.doc('list_of_seats_in_audi')
    @spi.marshal_list_with(_seat, envelope='data')
    def get(self):
        """List all seats in audi"""
        return get_all_seats()

    @spi.response(201, 'Seats successfully created.')
    @spi.doc('create a new SeatMap')
    @spi.expect(_seat, validate=True)
    def post(self):
        """Creates a new seatmap """
        data = request.json
        return init_seats(data=data)


@spi.route('/<seat_no>')
@spi.param('r,c', 'row and column')
@spi.response(404, 'Seat not in audi')
class Seat(Resource):
    @spi.doc('get a seat')
    @spi.marshal_with(_seat)
    def get(self, public_id):
        """get a seat given its identifier"""
        seat = get_a_seat(r,c)
        if not seat:
            spi.abort(404)
        else:
            return seat