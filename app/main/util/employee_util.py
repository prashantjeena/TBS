from flask_restplus import Namespace, fields


class EmployeeDto:
    api = Namespace('Employee', description='Employee related operations')
    emp = api.model('Employee', {
    	'emp_id':fields.String(required=True, description='employee id'),
        'username': fields.String(required=True, description='employee username'),
        'password': fields.String(required=True, description='employee password'),
        'public_id': fields.String(description='employee Identifier')
    })

class EmpAuthDto:
    api = Namespace('Empauth', description='employee authentication related operations')
    emp_auth = api.model('emp_auth_details', {
        'emp_id': fields.String(required=True, description='The employee id '),
        'password': fields.String(required=True, description='The employee password '),
    })