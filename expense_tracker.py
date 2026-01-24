from datetime import datetime
import argparse
from commands import commands as cmd

class Expense:
    def __init__(self, description, amount, category):
        self.id = 0
        self.description = description
        self.amount = amount
        self.dateAdded = datetime.now().isoformat()
        self.category = category

    def __str__(self):
        return f"ID: {str(self.id)}, Description: {self.description}, Amount: {str(self.amount)}, Date Added: {self.dateAdded}"

    @classmethod
    def create(cls, description, amount, category):
        return Expense(description, amount, category)

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("-d", "--description", help="Description of Expense")
    add_parser.add_argument("-a", "--amount", help="Amount of Expense", type=float)

    update_parser = subparsers.add_parser("update", help="Update an expense")
    update_parser.add_argument("-i", "--id", help="ID of Expense", type=int)
    update_parser.add_argument("-c", "--category", help="Type of Expense")

    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("-i", "--id", help="ID of Expense", type=int)

    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.add_argument("-m", "--month", help= "Month", type=int)
    list_parser.add_argument("-f", "--filter", help="Filter by category", type=str)

    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("-m", "--month", help="Month", type=int)

    export_parser = subparsers.add_parser("export", help="Export to csv")

    arguments = parser.parse_args()

    if arguments.command == "add":
        categories = ["bills", "food", "entertainment", "general",
                      "gifts", "groceries", "personal care", "shopping", "transport"]

        print(f"Select a category for this expense. Choose from the following: {categories}")
        category = input("Enter category name: ")

        expense = Expense.create(arguments.description, arguments.amount, category)
        cmd.add_expense(expense)

    if arguments.command == "update":
        cmd.update_expense(arguments.id, arguments.category)

    if arguments.command == "delete":
        cmd.delete_expense(arguments.id)

    if arguments.command == "list":
        cmd.list_expenses(arguments.month, arguments.filter)

    if arguments.command == "summary":
        cmd.summary(arguments.month)

    if arguments.command == "export":
        cmd.convert_to_csv()

if __name__ == "__main__":
    main()