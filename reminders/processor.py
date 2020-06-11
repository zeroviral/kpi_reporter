# Takes CSV as input
# Creates pandas object -> JSON
from pprint import pprint
import pandas as pd
import datetime
import time


def get_reminders_from_csv():
    """
    takes a CSV as input and returns a remindersJSON object
    :return: JSON representation of the input csv
    """
    reminders = pd.read_csv('demo_reminders.csv', header=None)
    reminders = reminders.rename({0: 'reminder'}, axis=1)
    remindersJSON = reminders.to_json(orient='records')
    return remindersJSON


def add_datestamp():
    """
    takes a remindersJSON object and injects the current
    time and date
    :return: reminderJSON
    """



if __name__ == "__main__":
    run()
