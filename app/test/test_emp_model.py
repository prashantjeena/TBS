import unittest
import datetime

from app.main import db
from app.main.model.employee import Employee
from app.test.base import BaseTestCase


class TestEmpModel(BaseTestCase):

    def test_encode_auth_token(self):
        emp = Employee(
            emp_id='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(emp)
        db.session.commit()
        auth_token = emp.encode_auth_token(emp.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        emp = Employee(
            emp_id='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(emp)
        db.session.commit()
        auth_token = emp.encode_auth_token(emp.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(Employee.decode_auth_token(auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()