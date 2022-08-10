from db import db
from werkzeug.security import generate_password_hash



class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    role = db.Column(db.String(10))

    # reserves = db.relationship('ReservesModel', lazy='dynamic')


    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = self._generate_password_hash(password) 
        self.role = role
    
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @staticmethod
    def _generate_password_hash(password_plain: str):
        return generate_password_hash(password_plain)
