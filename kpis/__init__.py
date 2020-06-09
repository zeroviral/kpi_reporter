import os
import sqlite3
import shelve
import time
import uuid
import datetime
from flask_restful import Resource, Api, reqparse
from markdown import markdown
from flask import Flask, g
from json import JSONEncoder

# Just creating an instance of Flask...
kpi_producer = Flask(__name__)

# Now creating the API...
kpi_api = Api(kpi_producer)


# Initialize our DB.
def get_db():
    if 'db' not in g:
        # g.db = sqlite3.connect(
        #     current_app.config['DATABASE'],
        #     detect_types=sqlite3.PARSE_DECLTYPES
        # )
        g.db = shelve.open("kpis.db")
        g.db.row_factory = sqlite3.Row

    return g.db


# Close DB once the server is terminated.
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def create_uuid():
    """
    Creates a unique string identifier for use in our db.
    :return: Unique string ID.
    """
    return uuid.uuid4().hex


def get_timestamp():
    """
    Return current timestamp.
    Output value ex: 2018-12-25 09:27:53
    :return:
    """
    return str(datetime.datetime.fromtimestamp(time.time()).strftime(
        '%m-%d-%Y %I:%M:%S%p'))


@kpi_producer.route("/")
def index():
    """
    Present the readme at the index, duh...
    :return: The readme.
    """
    with open(os.path.dirname(kpi_producer.root_path) + '/README.md', 'r') as readme:

        content = readme.read()

        # Returns an HTML readable format.
        return markdown(content)


class KPIList(Resource):
    """
    Endpoint for dealing with the KPIs list.
    """

    # Each HTTP verb requires a method to be able to interact with each
    # endpoint.
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        kpis = []

        for key in keys:
            kpis.append(shelf[key])

        # Return our payload in the following format.
        return {'message': 'Success', 'data': kpis}

    def post(self):
        parser = reqparse.RequestParser()

        # Initialize our payload and the serialized object.
        parser.add_argument('title_of_kpi', required=True)
        parser.add_argument('group', required=True)
        parser.add_argument('kpi_info', required=True)

        # We want to add a unique ID each time to the KPI.
        # This will help with data analysis down the line.
        # TODO: Figure out how to best implement this outside of argsparser.
        parser.add_argument('identifier', required=False)
        parser.add_argument('created_at', required=False)

        # Parse the arguments into an object
        args = parser.parse_args()

        # Here we can set the parameters uniquely.
        args.identifier = create_uuid()


        args.created_at = get_timestamp()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'KPI Registered', 'data': args}, 201


class KPI(Resource):
    """
    Endpoint for dealing with specified KPIs individually.
    """
    def get(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if identifier not in shelf:
            return {'message': 'KPI not found', 'data': {}}, 404

        return {'message': 'KPI found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'KPI not found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204


# Create our endpoints.
# Endpoint for interacting with the KPIList() object and its methods.
kpi_api.add_resource(KPIList, '/kpis')

# Endpoint for interacting with the KPI() object and its methods.
kpi_api.add_resource(KPI, '/kpis/<string:identifier>')