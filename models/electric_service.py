from db import db


class ElectricServiceModel(db.Model):
    __tablename__ = 'inegi_indicators'

    # structure of table in the database
    id = db.Column(db.Integer, primary_key=True)
    CITY = db.Column(db.String(100))
    VALUE = db.Column(db.Float)

    def __init__(self, CITY, VALUE, id):
        self.city = CITY
        self.value = VALUE
        self.id = id

    def json(self):
        return {
            'id': self.id,
            'city': self.CITY,
            'value': self.VALUE
        }

    @classmethod
    def find_by_city_name(cls, city):
        return cls.query.filter_by(CITY=city).first()
