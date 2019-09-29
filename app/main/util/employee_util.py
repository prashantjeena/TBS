from flask_restplus import Namespace, fields


class EmployeeDto:
    api = Namespace('Employee', description='Employee related operations')
    emp = api.model('Employee', {
    	'emp_id':fields.String(required=True, description='employee id'),
        'username': fields.String(required=True, description='employee username'),
        'password': fields.String(required=True, description='employee password'),
        'public_id': fields.String(description='employee Identifier')
    })