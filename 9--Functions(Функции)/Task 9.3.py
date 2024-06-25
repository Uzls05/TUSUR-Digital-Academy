# Example data
students = [
    ["Ivanov", "Ivan", "Ivanovich", 1998, 2, 101, [4, 5, 4, 3, 5]],
    ["Petrov", "Petr", "Petrovich", 1997, 2, 101, [3, 4, 5, 4, 3]],
    ["Sidorov", "Sidor", "Sidorovich", 1996, 2, 102, [5, 5, 4, 5, 4]],
    ["Kuznetsov", "Kuzma", "Kuznetsovich", 1998, 3, 201, [4, 3, 5, 4, 5]],
    ["Vasiliev", "Vasiliy", "Vasilievich", 2000, 3, 201, [5, 4, 4, 5, 4]],
    ["Smirnov", "Smir", "Smirnovich", 1995, 2, 102, [4, 5, 4, 3, 5]],
    ["Lebedev", "Lev", "Lebedevich", 2002, 2, 101, [3, 4, 5, 4, 3]],
    ["Semenov", "Semen", "Semenovich", 1996, 3, 202, [5, 5, 4, 5, 4]],
    ["Novikov", "Nikolai", "Novikovich", 1998, 3, 202, [4, 3, 5, 4, 5]],
    ["Fedorov", "Fedor", "Fedorovich", 1999, 3, 202, [5, 4, 4, 5, 4]],
]


def students_by_course(students, course):
    """
    Возвращает список студентов по курсу в алфавитном порядке
    """
    return sorted([student for student in students if student[4] == course], key=lambda x: x[0])


def average_grades_by_group(students):
    """
    Возвращает словарь со средними оценками по каждой группе и каждому предмету.
    """
    groups = {}
    for student in students:
        group = student[5]
        if group not in groups:
            groups[group] = []
        groups[group].append(student[6])
    averages = {}
    for group, grades in groups.items():
        averages[group] = [sum(subject) / len(subject) for subject in zip(*grades)]
    return averages


def oldest_and_youngest(students):
    """
    Возвращаются самые старшие и самые юные ученики.
    """
    oldest = min(students, key=lambda x: x[3])
    youngest = max(students, key=lambda x: x[3])
    return oldest, youngest


def best_students_by_group(students):
    """
    Возвращает словарь с лучшим учеником для каждой группы, основанный на общем среднем балле.
    """
    groups = {}
    for student in students:
        group = student[5]
        if group not in groups:
            groups[group] = []
        groups[group].append(student)
    best_students = {}
    for group, students_in_group in groups.items():
        best_students[group] = max(students_in_group,
                                   key=lambda x: sum(sum(sub) for sub in x[6:]) / sum(len(sub) for sub in x[6:]))
    return best_students


print(students_by_course(students, 3), end='\n\n')

print(average_grades_by_group(students), end='\n\n')

oldest, youngest = oldest_and_youngest(students)
print("Oldest:", oldest)
print("Youngest:", youngest, end='\n\n')

print(best_students_by_group(students))
