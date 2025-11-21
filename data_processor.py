from datetime import date
import csv

def validate_amount(amount) -> float:
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Input must be larger or equal to 0")

        return amount

    except ValueError:
        print("Input the initial amount as a number")


def create_initial_csv(initial_amount: float | int) -> None:
    amount = validate_amount(initial_amount)

    header_rows = ["Date", "Amount Spent", "Remainder"]
    first_row = [date.today().strftime("%d-%m-%Y"), "0", str(initial_amount)]

    with open(f"data/daily-spending.csv", "w") as csv_file:
        csv_file.writelines([",".join(header_rows), "\n", ",".join(first_row)])
        # TODO - Write this functionality using csv.writer instead.
