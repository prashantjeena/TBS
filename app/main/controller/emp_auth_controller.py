from flask import request
from flask_restplus import Resource

from app.main.service.emp_auth_helper import EmpAuth
from ..util.employee_util import EmpAuthDto

api = EmpAuthDto.api
emp_auth = EmpAuthDto.emp_auth


@api.route('/login')
class EmpLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('employee login')
    @api.expect(emp_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return EmpAuth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout an employee')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return EmpAuth.logout_user(data=auth_header)