from reminders.utils import database_utils
from reminders.utils.custom_logger import CustomLogger
from flask_restful import Resource


class RemindersList(Resource):
    """
    Endpoint for dealing with the reminders list.
    """

    def __init__(self):
        self.logger = CustomLogger()

    # Each HTTP verb requires a method to be able to interact with each
    # endpoint.
    def get(self):
        shelf = database_utils.get_db()
        keys = list(shelf.keys())

        reminders = []

        for key in keys:
            reminders.append(shelf[key])

        self.logger.logger.info("GET Request served successfully")

        # Return our payload in the following format.
        return {'message': 'Success', 'data': reminders}