

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        sum_grade = 0
        qt_grades = 0

        for x in self.grades.values():
            for grade in x:
                sum_grade = sum_grade + int(grade)
                qt_grades = qt_grades + len(x)
        avg_grade = sum_grade / qt_grades

        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)

        return (f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за ДЗ: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def rate_lector(self, lector, course, grade):
        if int(grade) > 10 or  int(grade < 0):
            print('Оценка может быть меньше 0 и больше10 ')
            return
        if course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            print('Ошибка курс студент не проходит этот курс или лектор его не читает')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def __str__(self):
        sum_grade = 0
        qt_grades = 0

        for x in self.grades.values():
            for grade in x:
                sum_grade = sum_grade + int(grade)
                qt_grades = qt_grades + len(x)
        avg_grade = sum_grade / qt_grades
        return (f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}" )


class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname}" )

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress += ['Python']
student.courses_in_progress += ['C++']
student.courses_in_progress += ['Sed']

cool_review = Reviewer('Some review', 'Buddy')
cool_review.courses_attached += ['Python']
cool_review.courses_attached += ['C']

cool_review.rate_hw(student, 'Python', 10)
cool_review.rate_hw(student, 'C', 2) # в реальности надо было бы сообщить что он не может оценить курс
print(student.grades)


cool_lecturer = Lecturer('Lecturer', 'Surname')
student.rate_lector(cool_lecturer, course='R', grade=3)
print(cool_lecturer.grades)

cool_lecturer.courses_attached += ['Python']
student.rate_lector(cool_lecturer, course='Python', grade=3)
print(cool_lecturer.grades)


# __str
print("===== Review")
print(cool_review)

cool_lecturer.courses_attached += ['C++']
student.rate_lector(cool_lecturer, course='C++', grade=10)
print('=== Лектор')
print(cool_lecturer)

cool_review.courses_attached += ['Sed']
cool_review.rate_hw(student, 'Sed', 2)

print('=== Студент')

student.finished_courses += [' Основы Python']
print(student)

