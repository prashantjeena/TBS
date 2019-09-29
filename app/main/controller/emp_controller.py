from flask import request
from flask_restplus import Resource

from ..util.employee_util import EmployeeDto
from ..service.emp_service import save_new_employee, get_all_employees, get_an_employee

api = EmployeeDto.api
_emp = EmployeeDto.emp


@api.route('/')
class EmployeeList(Resource):
    @api.doc('list_of_registered_employees')
    @api.marshal_list_with(_emp, envelope='data')
    def get(self):
        """List all registered employees"""
        return get_all_employees()

    @api.response(201, 'Employee successfully created.')
    @api.doc('create a new employee')
    @api.expect(_emp, validate=True)
    def post(self):
        """Creates a new employee """
        data = request.json
        return save_new_employee(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The employee identifier')
@api.response(404, 'Employee not found.')
class Employee(Resource):
    @api.doc('get an employee')
    @api.marshal_with(_emp)
    def get(self, public_id):
        """get an employee given its identifier"""
        employee = get_an_employee(public_id)
        if not employee:
            api.abort(404)
        else:
            return employee