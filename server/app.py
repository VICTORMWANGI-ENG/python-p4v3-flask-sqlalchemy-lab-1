# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response,jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


@app.route('/earthquakes')
def earthquakes():
    quakes = Earthquake.query.all()
    response=[{
        'id': eq.id,
        'magnitude': eq.magnitude,
        'location': eq.location,
        'year': eq.year
    }for eq in quakes]
    return make_response(jsonify(response), 200) 

@app.route('/earthquakes/<int:id>')
def earthquake_by_id(id):
    eq = Earthquake.query.get(id)
    if eq is None:
        return make_response({
            'message': f'Earthquake {id} not found.'
        }, 404)
    return make_response({
        'id': eq.id,
        'magnitude': eq.magnitude,
        'location': eq.location,
        'year': eq.year
        }, 200)


@app.route('/earthquakes/magnitude/<float:magnitude>')  
def earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()  
    quake_list = [{
        'id': eq.id,
        'location': eq.location,
        'magnitude': eq.magnitude,
        'year': eq.year
    } for eq in quakes]

    return make_response({
        'count': len(quake_list),
        'quakes': quake_list
    }, 200)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
