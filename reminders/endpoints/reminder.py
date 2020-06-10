from reminders.utils import database_utils
from flask_restful import Resource


class Reminder(Resource):
    """
    Endpoint for dealing with specified reminders individually.
    """
    @staticmethod
    def get(identifier):
        shelf = database_utils.get_db()

        # If the key does not exist in the data store, return a 404 error.
        # TODO: Change this to the database lookup.
        if identifier not in shelf:
            return {'message': 'Reminder not found', 'data': {}}, 404

        return {'message': 'Reminder found', 'data': shelf[identifier]}, 200

    @staticmethod
    def delete(identifier):
        shelf = database_utils.get_db()

        # If the key does not exist in the data store, return a 404 error.
        # TODO: Change this to database lookup.
        if identifier not in shelf:
            return {'message': 'Reminder not found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204
