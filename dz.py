
import statistics
from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def _average_grades_(self):
        grades = list(self.grades.values())
        new_list = []
        for index in grades:
           new_list += index
        avg = sum(new_list) / len(new_list) 
        return avg
    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f'{other} и {self} объекты разных классов')
        
        return self._average_grades_() < other._average_grades_()

       
        

    def __str__(self):
       course = ', '.join(self.courses_in_progress)
       finished_courses = ', '.join(self.finished_courses)
       res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._average_grades_()} \nКурсы в процессе изучения: {course} \nЗавершенные курсы: {finished_courses}'
       return res
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
    
    def _average_grades_(self):
        grades = list(self.grades.values())
        new_list = []
        for index in grades:
           new_list += index
        avg = sum(new_list) / len(new_list) 
        return avg
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(f'{other} и {self} объекты разных классов')
        
        return self._average_grades_() < other._average_grades_()
    
    def __str__(self):
       res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average_grades_()}'
       return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
       res = f'Имя: {self.name} \nФамилия: {self.surname}'
       return res





 


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['HTML']
# best_student.finished_courses += ['Введение в программирование']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# # cool_mentor.rate_hw(best_student, 'Python', 10)
# # cool_mentor.rate_hw(best_student, 'Python', 10)
# # cool_mentor.rate_hw(best_student, 'Python', 10)

# cool_reviewer = Reviewer('Irina', 'Krushelnitskays')
# cool_reviewer.courses_attached += ['Python']

# cool_lector = Lecturer('Vladimir', 'Ruban')
# cool_lector.courses_attached += ['Python']

# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_lw(best_student, 'HTML', 10)
# cool_reviewer.rate_lw(best_student, 'HTML', 8)
# cool_reviewer.rate_lw(best_student, 'HTML', 7)

# best_student.rate_lw(cool_lector, 'Python', 10)
# best_student.rate_lw(cool_lector, 'Python', 8)
# best_student.rate_lw(cool_lector, 'Python', 7)
# best_student.rate_lw(cool_lector, 'HTML', 10)
# best_student.rate_lw(cool_lector, 'HTML', 8)
# best_student.rate_lw(cool_lector, 'HTML', 7)


Student1 = Student('Julie', 'Ruban', 'ж')
Student1.courses_in_progress += ['Python']
Student1.courses_in_progress += ['HTML']
Student1.finished_courses += ['Введение в программирование']

Student2 = Student('Vladimir', 'Ruban', 'м')
Student2.courses_in_progress += ['Python']
Student2.courses_in_progress += ['HTML']
Student2.courses_in_progress += ['Statistics']
Student2.finished_courses += ['Введение в программирование']

Reviewer1 = Reviewer('Irina', 'Krushelnitskays')
Reviewer1.courses_attached += ['Python']
Reviewer1.courses_attached += ['HTML']

Reviewer2 = Reviewer('Marina', 'Medvedeva')
Reviewer2.courses_attached += ['Python']
Reviewer2.courses_attached += ['HTML']

Lector1 = Lecturer('Maxim', 'Flotskii')
Lector1.courses_attached += ['Python']
Lector1.courses_attached += ['HTML']

Lector2 = Lecturer('Oksana', 'Filatova')
Lector2.courses_attached += ['Python']

Student1.rate_lw(Lector1, 'Python', 8)
Student2.rate_lw(Lector1,'Python', 10)
Student1.rate_lw(Lector1, 'Python', 7)
Student2.rate_lw(Lector1,'Python', 9)

Student1.rate_lw(Lector1, 'HTML', 7)
Student2.rate_lw(Lector1,'HTML', 8)
Student1.rate_lw(Lector1, 'HTML', 9)
Student2.rate_lw(Lector1,'HTML', 10)

Student1.rate_lw(Lector2, 'Python', 10)
Student2.rate_lw(Lector2,'Python', 10)
Student1.rate_lw(Lector2, 'Python', 8)
Student2.rate_lw(Lector2,'Python', 9)

Reviewer1.rate_hw(Student1, 'Python', 7)
Reviewer2.rate_hw(Student1, 'Python', 9)
Reviewer1.rate_hw(Student1, 'HTML', 10)
Reviewer2.rate_hw(Student1, 'HTML', 10)

Reviewer1.rate_hw(Student2, 'Python', 7)
Reviewer2.rate_hw(Student2, 'Python', 9)
Reviewer1.rate_hw(Student2, 'HTML', 10)
Reviewer2.rate_hw(Student2, 'HTML', 10)




# print(Student1)
# print(Student2)
# print(Lector1)
# print(Lector2)
# print(Reviewer1)
# print(Reviewer2)
# print(Lector1.__lt__(Lector2))
# print(Student1.__lt__(Student2))

students = [Student1, Student2]    
lectors = [Lector1, Lector2]
def average_grade_students(students, course):
    grades = []
    for student in students:
       grades += student.grades[course]
    print(grades)
    avg = sum(grades) / len(grades)
    return avg

def average_grade_lectors(lectors, course):
    grades = []
    for lector in lectors:
       grades += lector.grades[course]
    print(grades)
    avg = sum(grades) / len(grades)
    return avg


print(average_grade_students(students, 'Python'))
print(average_grade_students(lectors, 'Python'))


