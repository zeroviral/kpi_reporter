from reminders import database_utils
from flask_restful import Resource


class Reminder(Resource):
    """
    Endpoint for dealing with specified reminders individually.
    """
    @staticmethod
    def get(identifier):
        shelf = database_utils.get_db()

        # If the key does not exist in the data store, return a 404 error.
        if identifier not in shelf:
            return {'message': 'reminders not found', 'data': {}}, 404

        return {'message': 'reminders found', 'data': shelf[identifier]}, 200

    @staticmethod
    def delete(identifier):
        shelf = database_utils.get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'reminders not found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204
