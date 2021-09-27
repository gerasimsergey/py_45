# просто как упражение для себя сделал рефакторинг
# не судите строго, ниже вопросы

# Может оцениватся
class Gradable:
    def __init__(self): # метод нужен только для инициализации grades
        self.grades = {}

        def get_grade_for_curs(self, curs):
            result = 0;
            curs_grades = self.grades.get(curs)
            if not curs_grades:
                return 0  # не правильно, но уже лень писать проверки
            cnt = len(curs_grades)
            for g in curs_grades:
                result = result + int(g)
            if cnt > 0:
                result = result / cnt
            return result

        def avg_grade(self):
            sum_grade = 0
            qt_grades = 0

            for x in self.grades.values():
                for grade in x:
                    sum_grade = sum_grade + int(grade)
                    qt_grades = qt_grades + len(x)

            if qt_grades > 0:
                avg_grade = sum_grade / qt_grades
                return avg_grade
            else:
                return

class Student(Gradable):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        super(Gradable, self).__init__()

    def __str__(self):
        avg_grade = self.avg_grade()

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


class Lecturer(Mentor, Gradable):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        # super(Gradable, self).__init__()
        super(Gradable).__init__()

    # def __init__(self, name, surname):
    #     super(Mentor, self).__init__(name,surname)
    #     super(Gradable, self).__init__()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not Lecturer')
            return
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        avg_grade = self.avg_grade()
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

print('=============')
print('Полевые испытания')

student1 = Student('Студент1', 'Первый', ' пол1')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['C++']

student2 = Student('Студент2', 'Второй', ' пол2')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['C++']

lecturer1 = Lecturer('Первый препод', 'Surname')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Второй препод', 'Surname')
lecturer2.courses_attached += ['Python']

student1.rate_lector(lecturer1, course='Python', grade=3)
student2.rate_lector(lecturer2, course='Python', grade=5)

cool_review1 = Reviewer('Some review 1', 'Buddy')
cool_review1.courses_attached += ['Python']
cool_review1.courses_attached += ['C++']

cool_review1.rate_hw(student1, 'Python', 10)
cool_review1.rate_hw(student2, 'C', 2)
cool_review1.rate_hw(student2, 'Python', 2)

cool_review2 = Reviewer('Some review 1', 'Buddy')

cool_review2.courses_attached += ['Python']
cool_review2.courses_attached += ['C++']

cool_review2.rate_hw(student1, 'Python', 5)
cool_review2.rate_hw(student2, 'C', 10)

print('Сравниваем лекторов, первый лучше?')
print(lecturer1 > lecturer2)

# !!! Метод __str__ вызывает все реализованые методы

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(cool_review1)
print(cool_review2)


print(student1.get_grade_for_curs('Python'))
print(student2.get_grade_for_curs('Python'))

# def evaluate_students(in_list, curs):
#     result = 0
#     cnt = len(in_list)
#     for st in in_list:
#         result = result + st.get_grade_for_curs(curs)
#     result = result / cnt
#     print(f"Средня оценка за ДЗ по курсу {curs} = {result}")
#
#
# def evaluate_lectors(in_list, curs):
#     result = 0
#     cnt = len(in_list)
#     for st in in_list:
#         result = result + st.get_grade_for_curs(curs)
#     result = result / cnt
#     print(f"Средня оценка за ДЗ по курсу {curs} = {result}")
#
#
# st_lst = [student1,student2]
# evaluate_students(st_lst,'Python' )
#
#
# evaluate_lectors([lecturer1, lecturer2],'Python' )


# так проще

def evaluate_persons(in_list, curs, eval_for):
    result = 0
    cnt = len(in_list)
    for st in in_list:
        result = result + st.get_grade_for_curs(curs)
    result = result / cnt
    print(f" {eval_for} {curs} = {result}")


st_lst = [student1,student2]
evaluate_persons(st_lst,'Python', 'Cреднaя оценки за ДЗ' )


evaluate_persons([lecturer1, lecturer2],'Python', 'Cредняя оценки за лекции'  )






