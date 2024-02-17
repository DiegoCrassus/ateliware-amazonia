import json
import unittest
from amazon.api.app import app as amazon_app


class TestAmazonia(unittest.TestCase):
    def setUp(self):
        amazon_app.testing = True
        self.app = amazon_app.test_client()

    def test_get(self):
        response = self.app.get("/api/status")
        assert response.status_code == 200

    def test_delivery(self):
        payload = {"start": "A1", "checkpoint": "C5", "finish": "G5"}
        expected_response = {
            "steps": ["A1", "B1", "C1", "C2", "C3", "C4", "C5", "D5", "E5", "F5", "G5"],
            "distance": 180.76,
        }

        response = self.app.post("/api/delivery/", json=payload)
        assert (
            response.status_code == 200
            and json.loads(response.data)["data"] == expected_response
        )

    def test_delivery_fail(self):
        payload = {"start": None, "checkpoint": "C5", "finish": "G5"}
        response = self.app.post("/api/delivery/", json=payload)
        assert response.status_code == 400
