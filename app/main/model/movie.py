from .. import db, flask_bcrypt
from sqlalchemy.orm import relationship

class Movie(db.Model):
    """ User Model for storing movie related details """
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    released_on = db.Column(db.DateTime)
    user_ratings=db.Column(db.Float)
    cast=db.Column(db.String(255))
    director=db.Column(db.String(255))
    duration_min=db.Column(db.Integer)
    description=db.Column(db.String(255))
    languages=db.Column(db.String(100))

    
    def __repr__(self):
        return "<movie '{}'>".format(self.title)

