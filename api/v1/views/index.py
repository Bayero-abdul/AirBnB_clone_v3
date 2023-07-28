'''This modules contains a route /status that 
returns a  a JSON: "status": "OK"'''

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def status():
    '''Returns a JSON: "status": "OK"'''
    status_dict = {"status": "OK"}
    return jsonify(status_dict)
