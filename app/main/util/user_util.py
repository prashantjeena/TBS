from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('end_user', description='user related operations')
    end_user = api.model('end_user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })