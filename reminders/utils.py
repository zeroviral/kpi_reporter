import uuid
import time
import datetime


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
