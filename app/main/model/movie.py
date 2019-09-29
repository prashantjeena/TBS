class Movie(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    released_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    user_ratings=Column(db.float(10), unique=True)
    cast=Column(db.string(255),nullabe=False)
    director=Column(db.string(255))
    duration_min=Column(db.int(10),nullabe=False)
    description=Column(db.String(255))
    price_movie=Column(db.int(10),nullabe=False)
    
    __tablename__ = ""

    
    def __repr__(self):
        return "<User '{}'>".format(self.username)
