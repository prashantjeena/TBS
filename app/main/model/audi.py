class Audi(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "audi"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    seats=db.Column(db.Integer)
    description=Column(db.String(255))
    
    
    def __repr__(self):
        return "<Audi '{}'>".format(self.name)