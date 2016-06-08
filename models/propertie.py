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

    @classmethod
    def find_in_area(cls, **kwargs):
        ax = kwargs.get("ax")
        bx = kwargs.get("bx")
        ay = kwargs.get("ay")
        by = kwargs.get("by")

        properties = cls.objects(
            x__lte=ax,
            x__gte=bx,
            y__lte=ay,
            y__gte=by
        )

        return [propertie.to_dict() for propertie in properties]

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
