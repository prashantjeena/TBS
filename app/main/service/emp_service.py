import uuid
import datetime

from app.main import db
from app.main.model.employee import Employee 


def save_new_employee(data):
    emp = Employee.query.filter_by(emp_id=data['emp_id']).first()
    if not emp:
        new_emp = Employee(
            public_id=str(uuid.uuid4()),
            emp_id=data['emp_id'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
            
        )
        save_changes(new_emp)
        response_object = {
            'status': 'success',
            'message': 'Employee Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Employee already exists. Please Log in.',
        }
        return response_object, 409


def get_all_employees():
    return Employee.query.all()


def get_an_employee(public_id):
    return Employee.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()