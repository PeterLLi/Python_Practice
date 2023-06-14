class Student(object):
    school_name = "University of Wisconsin - Milwaukee"

    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def set_grade(self, course, grade):
        self.grades[course] = grade

    def get_grade(self, course):
        return self.grades[course]

    def get_gpa(self):
        return sum(self.grades.values()) / len(self.grades)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_level(self):
        return self.level

    def birthday(self):
        self.age = self.age + 1
        return self.age

    def new_year(self):
        if self.level == "g1":
            self.level = "g2"
        elif self.level == "g2":
            print("Congratulations! You've graduated")
            self.level = "graduated"

    def get_year(self):
        return self.level


Peter = Student("Peter", 28, "Male", "g1", {'317': 4.0, '251': 4.0, '250': 2.5})

print(Peter.get_gpa())

Peter.set_grade('440', 4)
Peter.new_year()

print(Peter.get_gpa())
print(Peter.get_level())

Peter.new_year()

print(Peter.get_year())

Peter.birthday()

print(Peter.get_age())
print(Peter.name)
print(Student.school_name)
print(Peter.get_grade('317'))
