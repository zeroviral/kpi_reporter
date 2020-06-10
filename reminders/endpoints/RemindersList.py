import os
import sqlite3
import shelve
from reminders import database_utils
from reminders.utils import get_timestamp, create_uuid
from reminders.custom_logger import CustomLogger
from flask_restful import Resource, Api, reqparse
from markdown import markdown
from flask import Flask, g


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