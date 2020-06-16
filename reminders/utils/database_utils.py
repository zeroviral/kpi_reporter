import sqlite3
import shelve
from flask import Flask, g


# Initialize our DB.
def get_db():
    """
    Initialize and return a db instance.
    :return: A DB instance.
    """
    if 'db' not in g:
        # TODO: Replace with our mongoDB instance.
        # g.db = sqlite3.connect(
        #     current_app.config['DATABASE'],
        #     detect_types=sqlite3.PARSE_DECLTYPES
        # )
        g.db = shelve.open("reminders.db")
        g.db.row_factory = sqlite3.Row

    return g.db


# Close DB once the server is terminated.
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()