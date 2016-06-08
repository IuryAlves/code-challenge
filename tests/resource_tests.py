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
            provinces=["Ruja"],
            squareMeters=42
        ).save()

    def tearDown(self):
        pass

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
            "provinces": ['Scavy']
        }

        response = self.client.post("/properties", data=data)

        self.assertEqual(response.status_code, 200)

    def test_get_propertie(self):

        response = self.client.get("/properties/{id}".format(id=self.propertie_1.id))
        content = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(self.propertie_1.to_dict(), content)

