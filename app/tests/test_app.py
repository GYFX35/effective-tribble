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

    def test_get_optimal_route_missing_params(self):
        response = self.app.post(
            '/api/optimal_route',
            data=json.dumps({'destination': 'London, UK'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

class TestWeb(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Global Logistics and Transport Software!', response.data)

    def test_shipments_page(self):
        response = self.app.get('/shipments')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current Shipments', response.data)

    def test_tools_page(self):
        response = self.app.get('/tools')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logistics Tools', response.data)

    def test_companies_page(self):
        response = self.app.get('/companies')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Global Transport Companies', response.data)

if __name__ == '__main__':
    unittest.main()
