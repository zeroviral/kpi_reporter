from reminders import database_utils
from reminders import utils
from flask_restful import Resource, reqparse


class CreateReminder(Resource):
    """
    Endpoint for creating a SINGLE reminder.
    """

    @staticmethod
    def post():
        parser = reqparse.RequestParser()

        # Initialize our payload and the serialized object.
        parser.add_argument('title_of_reminder', required=True)
        parser.add_argument('completed', required=True)

        # We want to add a unique ID each time to the reminders.
        # This will help with data analysis down the line.
        # TODO: Figure out how to best implement this outside of argsparser.
        parser.add_argument('identifier', required=False)
        parser.add_argument('created_at', required=False)

        # Parse the arguments into an object
        args = parser.parse_args()

        # Here we can set the parameters uniquely.
        args.identifier = utils.create_uuid()
        args.created_at = utils.get_timestamp()

        shelf = database_utils.get_db()
        shelf[args['identifier']] = args

        return {'message': 'Reminder Registered', 'data': args}, 201
