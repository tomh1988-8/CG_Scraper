from datetime import datetime, time
from def_process_year import process_year


def is_before_5pm():
    now = datetime.now()
    return now.time() < time(17, 0)


if __name__ == "__main__":
    year = "2018"  # Change to the desired year
    while is_before_5pm():
        process_year(year)
