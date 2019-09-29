import uuid
import datetime

from app.main import db
from app.main.model.employee import Employee 


def save_new_user(data):
    emp = Employee.query.filter_by(email=data['email']).first()
    if not emp:
        new_user = Employee(
            public_id=str(uuid.uuid4()),
            emp_id=data['emp_id'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return Employee.query.all()


def get_a_user(public_id):
    return Employee.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()