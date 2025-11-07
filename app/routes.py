from app import app
from flask import jsonify, request, render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/shipments')
def shipments():
    return render_template('shipments.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/assistance')
def assistance():
    return render_template('assistance.html')

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
    if not data:
        return jsonify({'error': 'Invalid JSON payload.'}), 400

    origin = data.get('origin')
    destination = data.get('destination')

    if not origin or not destination:
        return jsonify({'error': 'Origin and destination are required.'}), 400

    route = get_optimal_route(origin, destination)
    return jsonify(route)
