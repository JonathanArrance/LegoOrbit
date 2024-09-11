#!/bin/python
import settings
import logging
import time
from orbit_lib import Orbit
from database import Database


#API Stuff
from flask import Flask, abort, jsonify, request
from flask_restx import Api, Resource, reqparse
from werkzeug.middleware.proxy_fix import ProxyFix
#from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

#Set flask to output "pretty print"
application = Flask(__name__)
application.secret_key = "arrance"
application.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
application.config['DEBUG'] = True
application.wsgi_app = ProxyFix(application.wsgi_app)

restxapi = Api(application,version=settings.APIVER, title='Lego Orbit API',
    description='An API used to interact with the Lego Orbit Model.',)

#Enable logging
logging.basicConfig(level=logging.DEBUG)

parser = reqparse.RequestParser()

#create the namespaces
ns1 = restxapi.namespace('orbit/', description='Lego Orbit API endpoints')

orb = Orbit()
db = Database()

@ns1.route('/listcoins')
class ListCoins(Resource):
    #@auth.login_required
    def get(self):
        return jsonify(db.get_coins())