# Global Logistics and Transport Software

This project is a global logistics and transport software designed to assist transport companies. It is a web-based application built with Flask that provides API endpoints for managing shipments and calculating optimal routes.

## Features

- **Shipment Management:** API endpoint to retrieve a list of current shipments.
- **Route Optimization:** API endpoint to calculate the optimal route for a shipment (currently a placeholder, with plans to integrate with Google Maps).
- **Web Interface:** A simple, user-friendly interface for interacting with the logistics data.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask development server:
   ```bash
   python3 run.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000` to view the application.

### Deployment

This application is ready to be deployed using Docker.

1. Build the Docker image:
   ```bash
   docker build -t logistics-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 logistics-app
   ```
3. Open your web browser and navigate to `http://localhost:8000` to view the application.
