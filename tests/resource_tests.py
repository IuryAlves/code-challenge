# coding: utf-8

import json
import unittest

from app import app
from models.propertie import Propertie


class ResourcesTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.propertie_1 = Propertie(
            title="Imóvel código 665, com 1 quarto e 1 banheiro",
            price=540000,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            x=667,
            y=556,
            beds=1,
            baths=1,
            squareMeters=42
        ).save()

    def tearDown(self):
        Propertie.drop_collection()

    def test_post_properties(self):
        data = {
            "x": 222,
            "y": 444,
            "title": u"Imóvel código 1, com 5 quartos e 4 banheiros",
            "price": 1250000,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "beds": 4,
            "baths": 3,
            "squareMeters": 210,
        }

        response = self.client.post("/properties", data=data)

        self.assertEqual(response.status_code, 201)

    def test_post_insufficient_params(self):
        data = {
            "x": 222,
            "y": 444,
            "title": u"Imóvel código 1, com 5 quartos e 4 banheiros",
            "price": 1250000,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "beds": 4,
            "baths": 3,
        }
        response = self.client.post("/properties", data=data)
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(content, {
            u'message': {
                u'squareMeters': u'Missing required parameter in the JSON body'
                                 u' or the post body or the query string'}})

    def test_get_property_by_id(self):

        response = self.client.get("/properties/{id}".format(id=self.propertie_1.id))
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(self.propertie_1.to_dict(), content)

    def test_get_property_with_insufficient_params(self):
        response = self.client.get("/properties")
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(content, {
            u'message': u"You must provide an id or a query string with 'ax', 'bx', 'ay', 'by"})

    def test_get_property_invalid_id(self):
        response = self.client.get("/properties/{id}".format(id=10))

        self.assertEqual(response.status_code, 404)

    def test_get_properties_by_area(self):
        ax, bx = (700, 300)
        ay, by = (600, 400)

        response = self.client.get("/properties?ax={ax}&bx={bx}&ay={ay}&by={by}".format(
            ax=ax,
            bx=bx,
            ay=ay,
            by=by
        ))
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(content, [self.propertie_1.to_dict()])
