import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger


logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        results = cursor.fetchall()

        for r in results:
            print(r)

def fetch_expenses_for_category(category):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE category = %s", (category,))
        results = cursor.fetchall()
        return results


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        results = cursor.fetchall()
        return results

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expenses called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date = %s", (expense_date,)
        )

def fetch_expense_summary_by_category(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            """SELECT category, SUM(amount) as total 
                        FROM expenses WHERE expense_date 
                        BETWEEN %s AND %s GROUP BY category""", (start_date, end_date)
        )
        result = cursor.fetchall()
        return result

def fetch_expense_summary_by_month():
    logger.info("fetch_expense_summary by month")
    with get_db_cursor() as cursor:
        cursor.execute(
            """SELECT MONTHNAME(min(expense_date)) AS month, SUM(amount) AS total
                FROM expenses GROUP BY month(expense_date) ORDER BY month(expense_date)""",
        )
        result = cursor.fetchall()
        return result


if __name__=="__main__":

    # expenses = fetch_expenses_for_date("2024-08-01")
    # print(expenses)

    # insert_expense("2024-08-25", 1500, "Travel", "Flight ticket")

    # expenses = fetch_expenses_for_date("2024-08-25")
    # print(expenses)
    #
    # delete_expenses_for_date("2024-08-25")
    #
    # expenses = fetch_expenses_for_date("2024-08-25")
    # print(expenses)

    # expenses = fetch_expenses_for_category("Rent")
    # total_amount = 0
    # for expense in expenses:
    #     print(expense['amount'])
    #     total_amount += float(expense['amount'])
    # print("Total rent amount: ", total_amount)

    # expenses = fetch_expense_summary_by_category("2024-07-01","2024-08-30")
    # for expense in expenses:
    #     print(expense)

    expenses = fetch_expense_summary_by_month()
    for expense in expenses:
        print(expense)


