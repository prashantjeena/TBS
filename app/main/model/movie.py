from .. import db, flask_bcrypt

class Movie(db.Model):
    """ User Model for storing movie related details """
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    released_on = db.Column(db.DateTime)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    user_ratings=Column(db.float(10))
    cast=Column(db.string(255))
    director=Column(db.string(255))
    duration_min=Column(db.int(10))
    description=Column(db.String(255))
    price_movie=Column(db.int(10),nullable=False)
    languages=Column(db.String(100))

    
    def __repr__(self):
        return "<movie '{}'>".format(self.title)

