#!/usr/bin/python3
"""
This module creates an endpoint that retrieves
the number of each objects by type
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Return the status of your API
    """
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    return dict count of data
    """
    stats = {"amenities": storage.count(Amenity),
             "cities": storage.count(City),
             "places": storage.count(Place),
             "reviews": storage.count(Review),
             "states": storage.count(State),
             "users": storage.count(User)}
    return jsonify(stats)
