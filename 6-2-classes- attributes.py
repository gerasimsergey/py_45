class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        self.grades = {}

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)

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

