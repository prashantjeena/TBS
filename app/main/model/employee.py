class Employee(db.Model):
    """ User Model for storing employee related details """
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    emp_id= db.Column(db.String(255),nullable=False,unique=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Employee '{}'>".format(self.username)