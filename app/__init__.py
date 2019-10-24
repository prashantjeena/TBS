# app/__init__.py

from flask_restplus import Api
from flask import Blueprint
from .main.controller.auth_controller import api as user_auth_ns
from .main.controller.emp_auth_controller import api as emp_auth_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.emp_controller import api as emp_ns
from .main.controller.theatre_controller import api as thtr_ns
from .main.controller.theatre_controller import bpi as audi_ns
from .main.controller.theatre_controller import spi as seat_ns
from .main.controller.theatre_controller import mpi as movie_ns
from .main.controller.booking_controller_admin import tpi as thtr1_ns
from .main.controller.booking_controller_admin import mpi as mov_ns
from .main.controller.booking_controller_admin import spi as show_ns
from .main.controller.booking_controller_admin import dpi as date_ns
from .main.controller.booking_controller_admin import stpi as slot_ns
from .main.controller.booking_controller_admin import api as audi_ns
from .main.controller.booking_controller_admin import cpi as seat_ns
from .main.controller.booking_controller_admin import rpi as rsrv_ns
from .main.controller.booking_controller import api as thtr2_ns 
from .main.controller.booking_controller import mpi as mov1_ns
from .main.controller.booking_controller import spi as slot1_ns
from .main.controller.booking_controller import sti as seat1_ns
from .main.controller.booking_controller import rpi as rsrv1_ns




blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(emp_ns, path='/emp')
api.add_namespace(user_auth_ns)
api.add_namespace(emp_auth_ns)
api.add_namespace(thtr_ns)
api.add_namespace(audi_ns)
api.add_namespace(seat_ns)
api.add_namespace(movie_ns)
api.add_namespace(thtr1_ns)
api.add_namespace(mov_ns)
api.add_namespace(show_ns)
api.add_namespace(date_ns)
api.add_namespace(slot_ns)
api.add_namespace(audi_ns)
api.add_namespace(seat_ns)
api.add_namespace(rsrv_ns)
api.add_namespace(thtr2_ns)
api.add_namespace(mov1_ns)
api.add_namespace(slot1_ns)
api.add_namespace(seat1_ns)
api.add_namespace(rsrv1_ns)
