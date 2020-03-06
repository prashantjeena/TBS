from .. import db, flask_bcrypt

class Seating(db.Model):
    """ User Model for storing auditorium related details """
    __tablename__ = "seating"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    row = db.Column(db.Integer, nullable=False)
    column = db.Column(db.Integer, nullable=False)
    seat_type = db.Column(db.String(10), nullable=False, default='silver')
    availability=db.Column(db.string(20),nullable=False, default='available')


    def __init__(self,row,column):

    	self.row=row
    	self.column=column
    	self.seat_no=(row,column)        
    
    def __repr__(self):
        return "<Seating '{}'>".format(self.seat_no)

