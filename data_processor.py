from datetime import date
import csv


today = date.today().strftime("%d-%m-%Y")
daily_csv_path = f"/data/daily-spendings/{today}.csv"


def print_error(error: Exception) -> None:
    print(f"Error: {error}")


def create_daily_csv():
    first_row = ["Amount Spent", "Description", "Balance"]
    with open(daily_csv_path, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(first_row)


def validate_daily_csv() -> None:
    try:
        with open(daily_csv_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            reader[0]
    except FileNotFoundError:
        create_daily_csv()


def validate_amount(amount) -> float:
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Input must be larger or equal to 0")

        return amount
    except ValueError as e:
        print_error(e)


def validate_description(description) -> str:
    try:
        if not isinstance(description, str):
            raise ValueError("Input must be a string")
        if len(description) < 3:
            raise ValueError("Input string must be longer than 3 characters")

        return description
    except ValueError as e:
        print_error(e)


def add_spending_to_daily_csv(
    amount_spent: float | int,
    description: str,
    balance: float | int,
) -> None:
    validate_daily_csv()
    amount = validate_amount(amount_spent)
    description = validate_description
    balance = validate_amount(balance)

    row = [str(amount), description, str(balance - amount)]

    with open(daily_csv_path, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)
