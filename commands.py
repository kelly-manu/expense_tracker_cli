import json
import os
from enum import Enum
from datetime import datetime
from matplotlib import pyplot as plt

expense_file = "expense_tracker.json"

class Months(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12

def get_month(month):
    """
    :param month: The month number
    :return: The name of the month
    """

    return Months(month).name

def save_expense(expense):
    """
    :param expense: The expense object that contains details of the expense
    :return: None. Saves the data back into the json file.
    """

    with open(expense_file, "w") as file:
        json.dump(expense, file, indent=4)

def load_expense():
    """
    Checks if the tracker file exists and creates a new file if it does not.
    Allows users to remove corrupt tracker files.

    :return: The data from the expense tracker json file.
    """
    if not os.path.exists(expense_file):
        return []
    try:
        with open(expense_file, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: The JSON file is corrupt.")
        user_input = input("Do you want to delete the corrupt file and proceed? (yes/no): ").strip().lower()
        if user_input == 'yes':
            os.remove(expense_file)
            print("The corrupt file has been deleted. Proceeding with an empty list.")
            return []
        else:
            print("Please delete the corrupt file manually to proceed.")
            exit(1)

