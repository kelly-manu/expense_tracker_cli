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

def generate_pie_chart(values, keys, month=None):
    """
    Generate a pie chart of expenses based on categories in a month or all-time
    :param values: Total amount spent on a category
    :param keys: The categories
    :param month: The month in which the pie chart will be generated (Optional)
    :return: None.
    """
    if month:
        plt.title(f"Expense chart for the month of {month}")

    else:
        plt.title(f"Expense chart")

    plt.pie(values, labels=keys, autopct="%1.1f%%")
    plt.show()

def add_expense(expense):
    """
    Adds an expense to the expense tracker file.
    :param expense: The expense object to be added
    :return: None.
    """

    if expense.amount <= 0:
        print("Amount cannot be less than 0")
        return

    expense.amount = float(expense.amount)
    if round(expense.amount, 2) != expense.amount:
        raise ValueError("Amount must be one or two decimal places!!")

    data = load_expense()

    if len(data) == 0:
        expense.id = 1

    else:
        expense.id = data[-1]["id"] + 1

    data.append({
        "id": expense.id,
        "description": expense.description,
        "amount": expense.amount,
        "dateAdded": expense.dateAdded,
        "category": expense.category,
        })

    save_expense(data)
    print(f"Expense added successfully! ID: {str(expense.id)}")

def update_expense(expense_id, update):
    """
    Updates the category of an expense
    :param expense_id: The ID of the expense to be updated
    :param update: The new category
    :return: None.
    """

    data = load_expense()
    for item in data:
        if item["id"] == expense_id:
            item["category"] = update
            save_expense(data)
            print(f"Expense with ID: {str(expense_id)} updated successfully!")
            return
    print(f"Expense with ID: {str(expense_id)} not found.")

def delete_expense(expense_id):
    """
    Deletes an expense from the expense tracker file.
    :param expense_id: The ID of the expense to be deleted.
    :return: None
    """

    data = load_expense()
    for item in data:
        if item["id"] == expense_id:
            data.remove(item)
            save_expense(data)
            print(f"Expense with ID: {str(expense_id)} deleted successfully!")
            return
    print(f"Expense with ID: {str(expense_id)} not found.")

def list_expenses(month=None, filter=None):
    """
    Lists the expenses in a category during a month or all-time OR
    Lists every expense ever added.

    :param month: The month of the expenses to be listed.
    :param filter: The category of the expenses

    :return: None
    """
    data = load_expense()
    total = 0
    index = 1
    if month is None:
        if filter:
            print(f"List of expenses filtered by {filter}:")
            for item in data:
                if item["category"] == filter:
                    print(f"{str(index)}. {datetime.fromisoformat(item['dateAdded']).strftime('%d-%m-%Y')} "
                          f"{item['description']} (ID: {item['id']}) -- £{item['amount']}")
                    index += 1
                    total += item["amount"]
            print(f"Total amount spent on {filter}: £{round(total,2)}")

        else:
            for item in data:
                print(f"{str(index)}. {datetime.fromisoformat(item['dateAdded']).strftime('%d-%m-%Y')} "
                      f"{item['description']} (ID: {item['id']}) -- £{item['amount']}")
                index += 1
                total += item["amount"]
            print(f"Total expense: £{round(total,2)}")

    else:
        if filter:
            print(f"List of expenses filtered by {filter} in {get_month(month)}:")
            for item in data:
                date = datetime.fromisoformat(item["dateAdded"]).month
                if date == month and item["category"] == filter:
                    print(f"{str(index)}. {datetime.fromisoformat(item['dateAdded']).strftime('%d-%m-%Y')} "
                          f"{item['description']} (ID: {item['id']}) -- £{item['amount']}")
                    index += 1
                    total += item["amount"]
            print(f"Total amount spent on {filter} in {get_month(month)}: {round(total,2)}")

        else:
            for item in data:
                date = datetime.fromisoformat(item["dateAdded"]).month
                if date == month:
                    print(f"{str(index)}. {datetime.fromisoformat(item['dateAdded']).strftime('%d-%m-%Y')} "
                          f"{item['description']} (ID: {item['id']}) -- £{item['amount']}")
                    total += item["amount"]
                    index += 1
            print(f"Total expense for the month of {get_month(month)}: £{round(total,2)}")

def summary(month=None):
    """
    Generates a pie chart to summarize the expenses.
    :param month: The specific month of the expenses to be summarized.
    :return: None
    """

    data = load_expense()
    data_dict = {}
    if month:
        for item in data:
            date = datetime.fromisoformat(item["dateAdded"]).month
            if date == month:
                item_category = item["category"]
                if item_category not in data_dict.keys():
                    data_dict[item_category] = item["amount"]

                else:
                    data_dict[item_category] += item["amount"]
        generate_pie_chart(data_dict.values(), data_dict.keys(), get_month(month))

    else:
        for item in data:
            item_category = item["category"]
            if item_category not in data_dict.keys():
                data_dict[item_category] = item["amount"]

            else:
                data_dict[item_category] += item["amount"]
        generate_pie_chart(data_dict.values(), data_dict.keys())