#!/usr/bin/python3
'''This modules contains a route /status that
returns a  a JSON: "status": "OK"'''

from models import storage
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=["GET"], strict_slashes=False)
def status():
    '''Returns a JSON: "status": "OK"'''
    status_dict = {"status": "OK"}
    return jsonify(status_dict)


@app_views.route('/stats', methods=['GET'])
def stats():
    '''Retrieves the number of each objects by type'''
    amenities = storage.count("Amenity")
    cities = storage.count("City")
    places = storage.count("Place")
    reviews = storage.count("Review")
    states = storage.count("State")
    users = storage.count("User")

    stats = {
        "amenities": amenities,
        "cities": cities,
        "places": places,
        "reviews": reviews,
        "states": states,
        "users": users,
    }

    return jsonify(stats)
