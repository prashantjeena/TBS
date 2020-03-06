import unittest
import datetime

from app.main import db
from app.main.model.user import EndUser
from app.test.base import BaseTestCase


class TestEndUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        User = EndUser(
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(User)
        db.session.commit()
        auth_token = User.encode_auth_token(User.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        User = EndUser(
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(User)
        db.session.commit()
        auth_token = User.encode_auth_token(User.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(EndUser.decode_auth_token(auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()
