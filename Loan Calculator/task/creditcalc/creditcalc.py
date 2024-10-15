"""
    The Loan Calculator calculates the annuity payments (monthly)
    or the differentiated payment (increases monthly) for loans based
    on the type of argument the user specifies.
"""
import argparse  # Used for command line arguments
import math
import sys


# Calculate the missing value needed
def calculate_loan_payment():
    parser = argparse.ArgumentParser()  # initialise an object

    # Arguments for the calculator
    parser.add_argument("--payment", type=float, help="The payment amount.")
    parser.add_argument("--interest", type=float,  help="The interest rate.")
    parser.add_argument("--principal", type=float, help="The principle amount.")
    parser.add_argument("--periods", type=int, help="The number of periods.")
    parser.add_argument("--type", help="The type of payment")

    args = parser.parse_args()  # get the values from the command-line
    # Check whether the values were 4 or more
    given_args = [args.payment, args.interest, args.principal, args.periods, args.type]
    number_of_args = check_args(given_args)
    if number_of_args < 4 or number_of_args > 5:
        print("Incorrect parameters")
        sys.exit()

    # Check for negative arguments
    for arg in given_args:
        if arg is not None and not isinstance(arg, str) and arg < 0:
            print("Incorrect parameters")
            sys.exit()

    # Check that the interest is provided
    if args.interest is None:
        print("Incorrect parameters")
        sys.exit()

    # Check which method to call
    if args.type == "annuity":
        calculate_annuity_payments(args.payment, args.principal, args.periods, args.interest)
    elif args.type == "diff":
        if args.payment is not None:
            print("Incorrect parameters")
            sys.exit()
        else:
            calculate_differentiated_payments(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters")
        sys.exit()


# Calculate the annuity payments
def calculate_annuity_payments(payment, principal, periods, interest):
    if payment is None:
        print(calculate_payment(principal, periods, interest))
    elif principal is None:
        print(calculate_principal(payment, periods, interest))
    elif periods is None:
        print(calculate_periods(payment, principal, interest))


# Calculate the differentiated payment
def calculate_differentiated_payments(principal, periods, interest):
    monthly_interest = interest / (12 * 100)
    all_payments = 0

    # Print the payment for each month
    for month in range(1, periods + 1):
        payments = (principal / periods) + monthly_interest * (principal - (principal * (month - 1) / periods))
        ceil_value = math.ceil(payments)
        all_payments += ceil_value
        print(f'Month {month}: payment is {ceil_value}')

    print()
    print(calculate_overpayment(principal, all_payments))


# calculate overpayment
def calculate_overpayment(principal, payments):
    overpayment = math.floor(payments - principal)
    return f'Overpayment = {overpayment}'


# Calculate the payment amount
def calculate_payment(principal, periods, interest):
    monthly_interest = interest / (12 * 100)
    payment = (principal * (monthly_interest * (1 + monthly_interest) ** periods)
               / ((1 + monthly_interest) ** periods - 1))
    ceil_value = math.ceil(payment)
    all_payments = ceil_value * periods

    # statement to return
    statement = f'Your annuity payment = {ceil_value}!'
    overpayment = calculate_overpayment(principal, all_payments)
    return f'{statement}\n{overpayment}'


# Calculate the principal amount
def calculate_principal(payment, periods, interest):
    monthly_interest = interest / (12 * 100)
    principal = payment * ((1 + monthly_interest) ** periods - 1) / (
                monthly_interest * (1 + monthly_interest) ** periods)
    floor_value = math.floor(principal)

    all_payments = payment * periods
    overpayment = calculate_overpayment(floor_value, all_payments)

    # statement to return
    statement = f'Your loan principal = {floor_value}!'
    return f'{statement}\n{overpayment}'


# Calculate the period in terms of months and years
def calculate_periods(payment, principal, interest):
    monthly_interest = interest / (12 * 100)
    periods = math.log(payment / (payment - monthly_interest * principal)) / math.log(1 + monthly_interest)
    ceil_value = math.ceil(periods)
    all_payments = ceil_value * payment

    overpayment = calculate_overpayment(principal, all_payments)

    # Check for singular or plural months and years
    years = ceil_value // 12
    months = ceil_value % 12
    result = ''

    if years >= 1:
        if years == 1:
            if months == 0:
                result = f'It will take {years} year to repay this loan!'
            elif months == 1:
                result = f'It will take {years} year and {months} month to repay this loan!'
            elif months > 1:
                result = f'It will take {years} year and {months} months to repay this loan!'
        elif years > 1:
            if months == 0:
                result = f'It will take {years} years to repay this loan!'
            elif months == 1:
                result = f'It will take {years} years and {months} month to repay this loan!'
            elif months > 1:
                result = f'It will take {years} years and {months} months to repay this loan!'
    elif years < 1:
        if months == 1:
            result = f'It will take {months} month to repay this loan!'
        elif months > 1:
            result = f'It will take {months} months to repay this loan!'
    return f'{result}\n{overpayment}'


def check_args(arg_values: list):
    return sum(value is not None for value in arg_values)


if __name__ == "__main__":
    calculate_loan_payment()
