# coding: utf-8


from app import db


class Propertie(db.Document):
    x = db.IntField(required=True)
    y = db.IntField(required=True)
    title = db.StringField(required=False)
    price = db.FloatField(required=False)
    description = db.StringField(required=False)
    beds = db.IntField(required=True)
    baths = db.IntField(required=True)
    provinces = db.DynamicField(required=False)
    squareMeters = db.FloatField(required=True)

    def to_dict(self):
        return {
            'x': self.x,
            'y': self.y,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'beds': self.beds,
            'baths': self.baths,
            'squareMeters': self.squareMeters

        }
