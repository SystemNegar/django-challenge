from db import db


class StadiumModel(db.Model):
    __tablename__ = 'stadium'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    address = db.Column(db.String(80))
    capacity = db.Column(db.Integer)

    items = db.relationship('MatchesModel', lazy='dynamic')

    def __init__(self, name, **kwargs):
        self.name = name
        self.city = kwargs["city"]
        self.address = kwargs["address"]
        self.capacity = kwargs["capacity"]

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'address': self.address,
            'capacity': self.capacity,            
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
