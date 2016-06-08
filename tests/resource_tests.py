# coding: utf-8

import json
import unittest

from src.app import app
from src.models.propertie import Propertie


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

    def test_post_properties_invalid_square_meters(self):
        data = {
            "x": 500,
            "y": 800,
            "title": u"Imóvel código 1, com 5 quartos e 4 banheiros",
            "price": 1250000,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "beds": 3,
            "baths": 2,
            "squareMeters": 250,
        }

        response = self.client.post("/properties", data=data)
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertDictEqual(content,
                             {u'message': u'squareMeters cannot be greater than 240 or lower than 20.'})

    def test_post_properties_invalid_number_of_bathrooms(self):
        data = {
            "x": 500,
            "y": 800,
            "title": u"Imóvel código 1, com 5 quartos e 4 banheiros",
            "price": 1250000,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "beds": 3,
            "baths": 0,
            "squareMeters": 210,
        }

        response = self.client.post("/properties", data=data)
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertDictEqual(content,
                             {u'message': u'The number of baths cannot be lower than 1 or greater than 4'})

    def test_post_properties_invalid_number_of_beds(self):
        data = {
            "x": 500,
            "y": 800,
            "title": u"Imóvel código 1, com 5 quartos e 4 banheiros",
            "price": 1250000,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "beds": 10,
            "baths": 3,
            "squareMeters": 210,
        }

        response = self.client.post("/properties", data=data)
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertDictEqual(content,
                             {u'message': u'The number of beds cannot be lower than 1 or greater than 5'})

    def test_post_properties_out_of_bounds(self):
        data = {
            "x": 1500,
            "y": 1200,
            "title": u"Imóvel código 1, com 5 quartos e 4 banheiros",
            "price": 1250000,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "beds": 4,
            "baths": 3,
            "squareMeters": 210,
        }

        response = self.client.post("/properties", data=data)
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertDictEqual(content,
                             {u'message':
                              u'x value cannot be lower than zero'
                              u' or greater than 1400.x is 1500'})

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

        response = self.client.get(
            "/properties/{id}".format(id=self.propertie_1.id))
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
        response = self.client.get(
            "/properties/{id}".format(id="4f4381f4e779897a2c000009"))

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
