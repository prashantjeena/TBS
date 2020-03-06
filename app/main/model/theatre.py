from .. import db
from sqlalchemy import Table, Column, Integer, ForeignKey,String,Boolean,DateTime,UniqueConstraint
from sqlalchemy.orm import relationship

class Theatre(db.Model):

    """ Model for storing Theatre related details """
    __tablename__ = "theatre"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    public_id = Column(String(100), unique=True)
    description=Column(String(255))
    base_price=Column(Integer,nullable=False,default=200)

    audi = relationship('Audi', backref='theatre',lazy='dynamic')
    movie = relationship('Movie', backref='theatre',lazy='dynamic')

    def __repr__(self):
        return "<Theatre '{}'>".format(self.name)

class Audi(db.Model):

    """ Model for storing auditorium related details """
    __tablename__ = "audi"
    __table_args__ = {'extend_existing': True}

    id=Column(Integer, primary_key=True,autoincrement=True)
    audi_name= Column(String(20),nullable=False)
    rows = Column(Integer, nullable=False)
    columns = Column(Integer, nullable=False)
    public_id = Column(String(100), unique=True)
    
    theatre_id = Column(Integer, ForeignKey('theatre.id'))
    slot= relationship('Slot', backref='audi',lazy='dynamic')
    seat=relationship('Seat', backref='audi',lazy='dynamic')
    movies=relationship('Movie', backref='audi',lazy='dynamic')
    showing=relationship('Showing', backref='audi',lazy='dynamic')

    def __repr__(self):
        return "<Audi : '{}'>".format(self.audi_name)

class Seat(db.Model):
    """ Model for storing seat related details """
    __tablename__ = "seat"
    __table_args__ = {'extend_existing': True}

    id=Column(Integer, primary_key=True,autoincrement=True)
    public_id = Column(String(100), unique=True)
    seat_type = Column(String(10), default='silver')
    seat_no=Column(String(5))
    seat_price=Column(Integer)

    audi_id = Column(Integer, ForeignKey('audi.id'))

    def __repr__(self):
        return "<Seat : '{}'>".format(self.seat_no)

class Movie(db.Model):
    """ User Model for storing movie related details """
    __tablename__ = "movie"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    public_id = Column(String(100), unique=True)
    released_on = db.Column(db.DateTime)
    user_ratings=db.Column(db.Float)
    cast=db.Column(db.String(255))
    director=db.Column(db.String(255))
    duration_min=db.Column(db.Integer)
    description=db.Column(db.String(255))
    Hindi=Column(Boolean(),default=False)
    English=Column(Boolean(),default=False)

    audi_id=Column(Integer, ForeignKey('audi.id'))
    date_id=Column(Integer, ForeignKey('date.id'))
    theatre_id = Column(Integer, ForeignKey('theatre.id'))
    showing=relationship('Showing', backref='movie',lazy='dynamic')

    def __repr__(self):
        return "<movie '{}'>".format(self.title)


    
class Showing(db.Model):
    __tablename__= "showing"
    __table_args__= {'extend_existing':True}
    __table_args__ = (UniqueConstraint('slot_id', 'movie_id', 'date_id', 'audi_id', name='showing_now'),)

    id= Column(Integer,primary_key=True,autoincrement=True)
    public_id=Column(String(100), unique=True)

    slot_id = Column(Integer, ForeignKey('slot.id'))
    movie_id= Column(Integer, ForeignKey('movie.id'))
    date_id = Column(Integer, ForeignKey('date.id'))
    audi_id = Column(Integer, ForeignKey('audi.id'))
    reservation=relationship('Reservation', backref='showing',lazy='dynamic')

class Slot(db.Model):
    """ Model for storing slot related details """
    __tablename__= "slot"
    __table_args__= {'extend_existing': True}

    id=Column(Integer,primary_key=True,autoincrement=True)
    slot_num=Column(Integer,nullable=False)
    time=Column(DateTime,nullable=False)

    
    audi_id = Column(Integer, ForeignKey('audi.id'))
    showing=relationship('Showing', backref='slot',lazy='dynamic')

class Date(db.Model):
    """ Model for storing Date related details """
    __tablename__= "date"
    __table_args__= {'extend_existing': True}
    id=Column(Integer,primary_key=True,autoincrement=True)
    date=Column(DateTime,nullable=False)

    movie=relationship('Movie', backref='date',lazy='dynamic')
    showing=relationship('Showing', backref='date',lazy='dynamic')

class Reservation(db.Model):
    __tablename__= "reservation"
    __table_args__ = (UniqueConstraint('seat_id', 'showing_id', name='ticket'),)

    id=Column(Integer,primary_key=True,autoincrement=True)
    status=Column(Boolean,default=True)

    seat_id = Column(Integer, ForeignKey('seat.id'))
    showing_id = Column(Integer, ForeignKey('showing.id'))

    def encode_auth_token(self, rsrv_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10, seconds=1),
                'iat': datetime.datetime.utcnow(),
                'sub': rsrv_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod  
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please select seats in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please select seats in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please select seats in again.'
