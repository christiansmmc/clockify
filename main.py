from core.clockify import Clockify
from core.salary import get_salary
from core.csv import to_csv


def main():
    clockify = Clockify()
    time_entry = clockify.get_time_entry()
    final_list = get_salary(time_entry)
    to_csv(final_list)
    print('CSV Created!')


if __name__ == "__main__":
    main()
