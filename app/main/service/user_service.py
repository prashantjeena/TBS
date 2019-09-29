import uuid
import datetime

from app.main import db
from app.main.model.user import EndUser


def save_new_user(data):
    user = EndUser.query.filter_by(email=data['email']).first()
    if not user:
        new_user = EndUser(
            public_id=str(uuid.uuid4()),
            email=data['email'],
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
    return EndUser.query.all()


def get_a_user(public_id):
    return EndUser.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()