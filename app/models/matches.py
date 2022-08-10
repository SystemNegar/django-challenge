"""
db model for match table

"""
from db import db


class MatchesModel(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    datetime = db.Column(db.String(80))
    teams = db.Column(db.String(80))
    capacity = db.Column(db.Integer)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'))

    def __init__(self, name: str, stadium_id: int, **kwargs):
        self.name = name
        self.stadium_id = stadium_id
        self.datetime = kwargs["datetime"]
        self.capacity = kwargs["capacity"]
        self.teams = kwargs["teams"]

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'datetime': self.datetime,
            'capacity': self.capacity,
            'teams': self.teams,
            'stadium_id': self.stadium_id
        }

    @classmethod
    def find_by_name(cls, name:str):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id:int):
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
