from src import db

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, username, email, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.email}, {self.password})'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }