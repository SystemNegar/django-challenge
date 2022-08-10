from db import db


class StadiumModel(db.Model):
    __tablename__ = 'stadium'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    address = db.Column(db.String(80))
    capacity = db.Column(db.Integer)
    number_of_segments = db.Column(db.Integer)
    segments = db.Column(db.String(200))

    items = db.relationship('MatchesModel', lazy='dynamic')

    def __init__(self, name, **kwargs):
        self.name = name
        self.city = kwargs["city"]
        self.address = kwargs["address"]
        self.capacity = kwargs["capacity"]
        self.number_of_segments = kwargs["number_of_segments"]
        self.segments = kwargs["segments"]

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'address': self.address,
            'capacity': self.capacity,            
            'number_of_segments': self.number_of_segments,            
            'segments': self.segments,            
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

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
