from flask import request
from flask_restplus import Resource

from ..util.theatre_util import TheatreDto,AudiDto,SeatDto,MovieDto
from ..service.theatre_service import save_new_theatre, get_all_theatres, get_a_theatre
from ..service.theatre_service import save_new_audi, get_all_audi, get_an_audi
from ..service.theatre_service import init_a_seat,get_audi_theatre,get_all_seats,get_a_seat
from ..service.theatre_service import save_new_movie, get_all_movies, get_a_movie,init_seats_in_audi

api = TheatreDto.api
_thtr = TheatreDto.thtr

bpi= AudiDto.api
_audi=AudiDto.audi

spi= SeatDto.api
_seat=SeatDto.seat

mpi = MovieDto.api
_mov = MovieDto.mov

# 1- theatre list
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
@api.response(404, 'Theatre not found.')
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


@bpi.route('/AudiT/<theatre_id>')
@bpi.param('theatre_id', 'The theatre id')
@bpi.response(404, 'audi not found.')

class AudiT(Resource):
    @bpi.doc('get an Audi in a theatre ')
    @bpi.marshal_with(_audi)
    def get(self, theatre_id):
        """get an audi given its theatre id"""
        audi = get_audi_theatre(theatre_id)
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
        return init_seats_in_audi(data=data)


@spi.route('/<public_id>')
@spi.param('public_id', 'public id of seat')
@spi.response(404, 'Seat not in audi')
class Seat(Resource):
    @spi.doc('get a seat')
    @spi.marshal_with(_seat)
    def get(self, public_id):
        """get a seat given its identifier"""
        seat = get_a_seat(public_id)
        if not seat:
            spi.abort(404)
        else:
            return seat

@mpi.route('/')
class Movies(Resource):
    @mpi.doc('list_of_movies')
    @mpi.marshal_list_with(_mov, envelope='data')
    def get(self):
        """List all seats in audi"""
        return get_all_movies()

    @mpi.response(201, 'movie successfully added')
    @mpi.doc('save a new movie')
    @mpi.expect(_mov, validate=True)
    def post(self):
        """save a new movie"""
        data = request.json
        return save_new_movie(data=data)


@mpi.route('/<public_id>')
@mpi.param('public_id', 'public id of movie')
@mpi.response(404, 'Movie not found')
class Mov(Resource):
    @mpi.doc('get a movie')
    @mpi.marshal_with(_mov)
    def get(self, public_id):
        """get a movie given its identifier"""
        movie = get_a_movie(public_id)
        if not movie:
            mpi.abort(404)
        else:
            return movie