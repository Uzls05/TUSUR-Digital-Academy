class Student:
    def __init__(self, id, name, group):
        self.id = id
        self.name = name
        self.group = group
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def get_average_grade(self):
        grades = [course.get_grade(self) for course in self.courses]
        return sum(grades) / len(grades)


class Group:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average_grade(self):
        grades = [student.get_average_grade() for student in self.students]
        return sum(grades) / len(grades)


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = {}

    def add_grade(self, student, grade):
        self.grades[student] = grade

    def get_grade(self, student):
        return self.grades.get(student)

    def get_average_grade(self):
        grades = list(self.grades.values())
        return sum(grades) / len(grades) if grades else 0


class Deanery:
    def __init__(self):
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def get_average_grades(self):
        group_grades = {}
        for group in self.groups:
            group_grades[group.name] = group.get_average_grade()
            course_grades = {}
            for course in group.students[0].courses:
                course_grades[course.name] = course.get_average_grade()
            group_grades[group.name] = course_grades
        return group_grades

# Example usage:
deanery = Deanery()

group1 = Group(1, "433")
group2 = Group(2, "434")

student1 = Student(1, "John", group1)
student2 = Student(2, "Jane", group1)
student3 = Student(3, "Bob", group2)

course1 = Course(1, "Physics")
course2 = Course(2, "Math")

student1.add_course(course1)
student1.add_course(course2)
student2.add_course(course1)
student3.add_course(course2)

course1.add_grade(student1, 4.5)
course1.add_grade(student2, 4.2)
course2.add_grade(student1, 3.8)
course2.add_grade(student3, 4.9)

group1.add_student(student1)
group1.add_student(student2)
group2.add_student(student3)

deanery.add_group(group1)
deanery.add_group(group2)

average_grades = deanery.get_average_grades()
print(average_grades)
