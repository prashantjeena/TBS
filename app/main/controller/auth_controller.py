from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import UserAuth
from ..util.user_util import UserAuthDto

api = UserAuthDto.api
user_auth = UserAuthDto.user_auth


@api.route('/userlogin')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        
        post_data = request.json
        return UserAuth.login_user(data=post_data)


@api.route('/userlogout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        
        auth_header = request.headers.get('Authorisation')
        return UserAuth.logout_user(data=auth_header)