# Takes CSV as input
# Creates pandas object -> JSON

import pandas as pd


def run():
    reminders = pd.read_csv('reminders.csv', header=None)
    print(reminders)

if __name__ == "__main__":
    run()
