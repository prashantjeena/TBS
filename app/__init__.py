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
