# coding: utf-8


from src.app import db


class Property(db.Document):
    x = db.IntField(required=True)
    y = db.IntField(required=True)
    title = db.StringField(required=False)
    price = db.FloatField(required=False)
    description = db.StringField(required=False)
    beds = db.IntField(required=True)
    baths = db.IntField(required=True)
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
            y__gte=ay,
            y__lte=by
        )

        return properties

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
