from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('EndUser', description='user related operations')
    EndUser = api.model('EndUser', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })