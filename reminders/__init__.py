import os
from reminders.utils import get_timestamp, create_uuid
from reminders import database_utils
from reminders.endpoints.Reminder import Reminder
from reminders.endpoints.RemindersList import RemindersList
from reminders.endpoints.CreateReminder import CreateReminder
from reminders.custom_logger import CustomLogger
from flask_restful import Api
from markdown import markdown
from flask import Flask

# Just creating an instance of Flask...
reminders_producer = Flask(__name__)

# Now creating the API...
reminders_producer_api = Api(reminders_producer)

# Set and nest the logger so we can access it globally, and singly as long as
# the current server instance is up.
logger = CustomLogger()
logger = logger.logger


@reminders_producer.route("/")
def index():
    """
    Present the readme at the index, duh...
    :return: The readme.
    """
    with open(os.path.dirname(reminders_producer.root_path) + '/README.md', 'r') as readme:
        content = readme.read()

        # Returns an HTML readable format.
        return markdown(content)


# Create our endpoints.
# Endpoint for interacting with RemindersList object and its methods.
# ACCEPTS: GET
reminders_producer_api.add_resource(RemindersList, '/reminders')

# Endpoint for interacting with a reminder.
# ACCEPTS: GET, DELETE
reminders_producer_api.add_resource(Reminder, '/reminders/<string:identifier>')

# Endpoint for creating a single reminder
# ACCEPTS: POST
reminders_producer_api.add_resource(CreateReminder, '/create_reminder')
