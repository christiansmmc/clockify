from config import SALARY_BASE


def get_salary(people: list):
    final_person_list = []

    for person in people:
        new_list = {
            'name': person['name'],
            'time_in_seconds': person['duration'],
            'salary': (person['duration'] // 3600) * int(SALARY_BASE)
        }

        final_person_list.append(new_list)

    return final_person_list
