from datetime import datetime, timedelta


def is_older_than_4_days(date_string):

    # Convert the string to a datetime object
    date_format = "%d.%m.%Y"
    given_date = datetime.strptime(date_string, date_format)

    # Get the current date
    current_date = datetime.now()

    # Calculate the difference
    date_difference = current_date - given_date

    # Check if the difference is more than 4 days
    is_older_than_4_days = date_difference > timedelta(days=4)

    return is_older_than_4_days