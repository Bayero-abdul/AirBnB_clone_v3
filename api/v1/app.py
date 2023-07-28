'''This module setup the application'''

import os
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['HOST'] = os.environ.get('HBNB_API_HOST', '0.0.0.0')
app.config['PORT'] = int(os.environ.get('HBNB_API_PORT', '5000'))
app.config['THREADED'] = True


@app.teardown_appcontext
def teardown_app(exception):
    """Closes a session"""
    storage.close()


if __name__ == "__main__":
     app.run(host=app.config['HOST'], port=app.config['PORT'], threaded=app.config['THREADED'])
