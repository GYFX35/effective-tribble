from app import app
from flask import jsonify, request

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to the Global Logistics and Transport Software!"

@app.route('/api/shipments', methods=['GET'])
def get_shipments():
    """
    API endpoint to retrieve a list of shipments.
    """
    shipments = [
        {
            'id': 'SH12345',
            'origin': 'New York, USA',
            'destination': 'London, UK',
            'status': 'In Transit'
        },
        {
            'id': 'SH67890',
            'origin': 'Shanghai, China',
            'destination': 'Los Angeles, USA',
            'status': 'Delivered'
        }
    ]
    return jsonify(shipments)

from app.ai import get_optimal_route

@app.route('/api/optimal_route', methods=['POST'])
def optimal_route():
    """
    API endpoint to get the optimal route for a shipment.
    """
    data = request.get_json()
    origin = data.get('origin')
    destination = data.get('destination')

    if not origin or not destination:
        return jsonify({'error': 'Origin and destination are required.'}), 400

    route = get_optimal_route(origin, destination)
    return jsonify(route)
