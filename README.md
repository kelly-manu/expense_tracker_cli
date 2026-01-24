## Expense Tracker

## Description
The Expense Tracker is a command line interface program designed to help users to manage their expenses. The program allows users to add, update, view and delete their expenses. It also provides a summary of their expenses.

This program uses the _**matplotlib**_ library to generate visual reports of the expenses.

It was inspired by the [Expense Tracker](https://www.roadmap.sh/project/expense-tracker) project from [roadmap.sh](https://www.roadmap.sh)
## Features
- **Add Expense**: Users can add new expenses with details such as description, amount and category.
- **Delete Expense**: Users can delete an expense.
- **Update Expense**: Users can update an expense by changing its category.
- **View Expenses**: Users can view a list of all expenses added.
- **View Expenses with filters**: Users can view a list of expenses filtered by month and category
- **Generate Reports**: Users can generate a chart of their expense for a specific month or every expense.

## Prerequisites
- Python 3.13.5
- Git
## Installation
1. Clone the repository:
```terminaloutput
git clone https://github.com/kelly-manu/expense_tracker_cli.git
cd expense_tracker_cli/
```
2. Create a Virtual Environment:
```terminaloutput
python -m venv venv
```
```terminaloutput
# Activate Environment on Windows:
.\venv\Scripts\activate.bat

# Activate on MacOS and Linux:
source venv/bin/activate
```
3. Install the dependencies:
```terminaloutput
pip install -r requirements.txt
```
## Use
```terminaloutput
python expense_tracker.py -h #Help
python expense_tracker.py add --description "Ticket" --amount 10.45 #Adds an expense
python expense_tracker.py update --id 1 --category "General" #Updates the category of the expense with ID: 1
python expense_tracker.py delete --id 1 # Deletes an expense
python expense_tracker.py list # Shows a list of all expenses added
python expense_tracker.py list --month 4 # Shows a list of all expenses added in April
python expense_tracker.py list --month 4 --filter "General" # Shows a list of all expenses in April under the General category
python expense_tracker.py list --filter "General" # Shows a list of every expense under the General category
python expense_tracker.py summary # Generates a pie-chart of all expenses in each category
python expense_tracker.py summary --month 4 # Generates a pie-chart based on the expenses added in April
python expense_tracker.py export # Exports expense data to a CSV file
```
