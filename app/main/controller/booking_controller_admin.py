from flask import request
from flask_restplus import Resource

from ..util.booking import BookingDto
from ..util.theatre_util import MovieDto,TheatreDto,ShowingDto,DateDto,SlotDto
from ..util.theatre_util import AudiDto,SeatDto,ReservationDto
from ..service.booking_service_admin import save_a_date,save_new_showing_details
from ..service.booking_service_admin import get_all_movie_from_a_theatre,save_a_slot
from ..service.booking_service_admin import get_a_movie,language_checker,save_a_reservation

tpi = TheatreDto.api
_thtr = TheatreDto.thtr

mpi=MovieDto.api
_mov=MovieDto.mov

spi=ShowingDto.api
_show=ShowingDto.show

dpi=DateDto.api
_dt=DateDto.dt

stpi=SlotDto.api
_slot=SlotDto.slot

api=AudiDto.api
_audi=AudiDto.audi

cpi=SeatDto.api
_seat=SeatDto.seat

rpi=ReservationDto.api
_rsrv=ReservationDto.rsrv


### 2 & 3- theatre list given

@mpi.route('/movie/<theatre_id>')
@mpi.param('theatre_id', 'The theatre identifier')
@mpi.response(404, 'No Movies found.')
class Movies(Resource):
    @mpi.doc('get all movies in theatre')
    @mpi.marshal_with(_mov)
    def get(self, theatre_id):
        """get all movies given their theater identifier"""
        movies = get_all_movie_from_a_theatre(theatre_id)
        if not movies:
            mpi.abort(404)
        else:
            return movies

###  provided movies in a theatre

@mpi.route('/movies/<title>')
@mpi.param('title', 'The movie title')
@mpi.response(404, 'movie not found.')
class MoviebyTitle(Resource):
    @mpi.doc('get a movie details by title ')
    @mpi.marshal_with(_mov)
    def get(self,title):
        """get a movie given its title """
        movie = get_a_movie(title)
        if not movie:
            mpi.abort(404)
        else:
            return movie

### provided movie details

@mpi.route('/moviel/<title>/<language>')
@mpi.param('t', 'The movie identifier')
@mpi.response(404, 'movie not found.')
class Language(Resource):
    @mpi.doc('Movie is available in Hindi')
    @mpi.marshal_list_with(_mov, envelope='data')
    def get(self,title,language):

        """ languages availability checker in a movie """

       # title  = request.args.get('title', None)
        #language  = request.args.get('language', None)
        movie=language_checker(title,language)
        if not movie:
            mpi.abort(404)
        else:
            return movie

###language checker

@spi.route('/')
class ShowList(Resource):
    @spi.response(201, 'Showing data successfully inserted.')
    @spi.doc('insert a new show details')
    @spi.expect(_show, validate=True)
    def post(self):
        """Inserts a new show details """
        data = request.json
        return save_new_showing_details(data=data)

@dpi.route('/')
class DateList(Resource):
    @dpi.response(201, 'Date successfully inserted.')
    @dpi.doc('insert a new date')
    @dpi.expect(_dt, validate=True)
    def post(self):
        """Inserts a new date """
        data = request.json
        return save_a_date(data=data)

@stpi.route('/')
class SlotList(Resource):
    @stpi.response(201, 'slot successfully inserted.')
    @stpi.doc('insert a new slot')
    @stpi.expect(_slot, validate=True)
    def post(self):
        """Inserts a new slot """
        data = request.json
        return save_a_slot(data=data)

@rpi.route('/')
class ReservationList(Resource):
    @rpi.response(201, 'Reservation successfully saved')
    @rpi.doc('save a new reservation')
    @rpi.expect(_rsrv, validate=True)
    def post(self):
        """Inserts a new slot """
        data = request.json
        return save_a_reservation(data=data)