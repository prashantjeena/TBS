from .. import db
from sqlalchemy import Table, Column, Integer, ForeignKey,String
from sqlalchemy.orm import relationship

class Theatre(db.Model):

    """ Model for storing Theatre related details """
    __tablename__ = "theatre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    public_id = Column(String(100), unique=True)
    description=Column(String(255))
    base_price=Column(Integer,nullable=False,default=200)

    def __repr__(self):
        return "<Theatre '{}'>".format(self.name)

class Audi(db.Model):

    """ Model for storing auditorium related details """
    __tablename__ = "audi"

    id=Column(Integer, primary_key=True,autoincrement=True)
    audi_name= Column(String(20),nullable=False)
    rows = Column(Integer, nullable=False)
    columns = Column(Integer, nullable=False)
    public_id = Column(String(100), unique=True)
    theatre_id = Column(Integer, ForeignKey('theatre.id'))

    def __repr__(self):
        return "<Audi : '{}'>".format(self.audi_name)

class Seat(db.Model):
    """ Model for storing seat related details """
    __tablename__ = "seat"

    id=Column(Integer, primary_key=True,autoincrement=True)   
    row = Column(String(1), nullable=False)
    column = Column(String(1), nullable=False)
    public_id = Column(String(100), unique=True)
    seat_type = Column(String(10), default='silver')
    seat_no=Column(String(5))
    seat_price=Column(Integer)
    status=Column(String(20),nullable=False,default='available')
    audi_id = Column(Integer, ForeignKey('audi.id'))
    

    def seatno(self,row,column):
    	self.seat_no=self.row+self.column

    def __repr__(self):
        return "<Seat : '{}'>".format(self.seat_no)


    