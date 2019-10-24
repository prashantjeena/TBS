from flask import request
from flask_restplus import Resource

from ..util.theatre_util import TheatreDto,AudiDto,SeatDto,MovieDto,SlotDto,DateDto,ReservationDto
from ..service.theatre_service import get_all_theatres
from ..service.booking_service import  get_all_movies, get_a_movie,get_all_movies_from_theatre,showtime
from ..service.booking_service import  seat_list,book_a_ticket


api = TheatreDto.api
_thtr = TheatreDto.thtr

mpi = MovieDto.api
_mov = MovieDto.mov

spi=SlotDto.api
_slo=SlotDto.slot

sti=SeatDto.api
_sto=SeatDto.seat

rpi=ReservationDto.api
_rsrv=ReservationDto.rsrv

@api.route('/')
class TheatreList(Resource):
    @api.doc('list_of_registered_theatres')
    @api.marshal_list_with(_thtr, envelope='data')
    def get(self):
        """List all registered theatres"""
        return get_all_theatres()


@mpi.route('/')
class Movies(Resource):
    @mpi.doc('list_of_movies')
    @mpi.marshal_list_with(_mov, envelope='data')
    def get(self):
        """List all movies"""
        return get_all_movies()

@mpi.route('/<theatre_id>')
@mpi.param('theatre_id', 'The theatre id')
@mpi.response(404, 'No movies found')
class MovieList(Resource):
    @mpi.doc('get all movies in a theatre')
    @mpi.marshal_with(_mov)
    def get(self, theatre_id):
        """get all movies given a theatre id"""
        movies = get_all_movies_from_theatre(theatre_id)
        if not movies:
            api.abort(404)
        else:
            return movies

@mpi.route('/audi/<theatre_id>')
@mpi.param('theatre_id', 'The theatre id')
@mpi.response(404, 'No movies found')
class MovieList(Resource):
    @mpi.doc('get all movies in a theatre')
    @mpi.marshal_with(_mov)
    def get(self, theatre_id):
        """get all movies given a theatre id"""
        movies = get_all_movies_from_theatre(theatre_id)
        if not movies:
            spi.abort(404)
        else:
            return movies

@spi.route('/slot/<movie_id>/<date_id>')
@spi.param('movie_id,date_id', 'The movie and date id')
@spi.response(404, 'No slots found')
class Showtime(Resource):
    @spi.doc('get all time slots for a given movie on a given date')
    @spi.marshal_with(_slo)
    def get(self, movie_id,date_id):
        """get all show timings for a movie id and a date id"""
        show = showtime(movie_id,date_id)
        if not show:
            spi.abort(404)
        else:
            return show


@sti.route('/seat/<movie_id>/<date_id>/<slot_id>')
@sti.param('movie_id,date_id,slot_id', 'The movie, date and slot id')
@sti.response(404, 'No seats available')
class Seats(Resource):
    @sti.doc('get all seats for a given show details')
    @sti.marshal_with(_slo)
    def get(self, movie_id,date_id,slot_id):
        """get a seat list for a show"""
        seats = seat_list(movie_id,date_id,slot_id)
        if not seats:
        	sti.abort(404)
        else:
        	return seats


@sti.route('/seat/<movie_id>/<date_id>/<slot_id>')
@sti.param('movie_id,date_id,slot_id', 'The movie, date and slot id')
@sti.response(404, 'No seats available')
class Seats(Resource):
    @sti.doc('get all seats for a given show details')
    @sti.marshal_with(_slo)
    def get(self, movie_id,date_id,slot_id):
        """get a seat list for a show"""
        seats = seat_list(movie_id,date_id,slot_id)
        if not seats:
        	sti.abort(404)
        else:
        	return seats

@rpi.route('/booking')
class Reservation(Resource):
	@rpi.response(201, 'Reservation successfully done.')
	@rpi.doc('book a ticket')
	@rpi.expect(_rsrv, validate=True)
	def post(self):
		"""book a ticket """
		data = request.json
		return book_a_ticket(data=data)
