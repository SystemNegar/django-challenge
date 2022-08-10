from db import db


class ReserveModel(db.Model):
    __tablename__ = 'reserves'

    id = db.Column(db.Integer, primary_key=True)
    segments = db.Column(db.String(80))
    row = db.Column(db.String(80))
    seat = db.Column(db.Integer)
    matches_id = db.Column(db.Integer, db.ForeignKey('matches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, **kwargs):
        self.segments = kwargs["segments"]
        self.row = kwargs["row"]
        self.seat = kwargs["seat"]
        self.matches_id = kwargs["matches_id"]
        self.user_id = kwargs["user_id"]

    def json(self):
        return {
            'id': self.id,
            'segments': self.segments,
            'row': self.row,
            'seat': self.seat,
            'matches_id': self.matches_id,
            'user_id': self.user_id
        }

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
        
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
