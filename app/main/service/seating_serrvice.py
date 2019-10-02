import uuid
import datetime

from app.main import db
from app.main.model.seating import Seating


def init_seats():

    for i in range(1,11):
        for j in range(1,11):
            db.session.add((Seating(i,j)))



def save_changes():
    db.session.commit()


