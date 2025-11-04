import unittest
import json
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_shipments(self):
        response = self.app.get('/api/shipments')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)

    def test_get_optimal_route(self):
        response = self.app.post(
            '/api/optimal_route',
            data=json.dumps({'origin': 'New York, USA', 'destination': 'London, UK'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('optimal_route', data)

if __name__ == '__main__':
    unittest.main()
