from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Przykładowe dane tras
routes = [
    {
        "id": 1,
        "name": "Trasa A",
        "waypoints": [
            {"description": "Punkt A1", "lat": 52.2297, "lng": 21.0122},
            {"description": "Punkt A2", "lat": 52.4064, "lng": 16.9252},
            {"description": "Punkt A3", "lat": 51.1079, "lng": 17.0385},
        ],
    },
    {
        "id": 2,
        "name": "Trasa B",
        "waypoints": [
            {"description": "Punkt B1", "lat": 50.0647, "lng": 19.9450},
            {"description": "Punkt B2", "lat": 50.0614, "lng": 19.9366},
            {"description": "Punkt B3", "lat": 50.0673, "lng": 19.9439},
        ],
    },
    {
        "id": 3,
        "name": "Trasa C",
        "waypoints": [
            {"description": "Punkt C1", "lat": 54.3520, "lng": 18.6466},
            {"description": "Punkt C2", "lat": 54.3672, "lng": 18.6333},
            {"description": "Punkt C3", "lat": 54.3953, "lng": 18.6322},
        ],
    },
]

@app.route('/')
def index():
    return render_template('index.html', routes=routes)

@app.route('/api/routes')
def get_routes():
    return jsonify(routes)

if __name__ == '__main__':
    app.run(debug=True)
