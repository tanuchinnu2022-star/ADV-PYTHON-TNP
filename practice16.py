class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student:", self.name)


class Teacher:
    def __init__(self, subject):
        self.subject = subject

    def show(self):
        print("Teaches:", self.subject)


class Admin:
    def manage(self):
        print("Admin manages school")


s = Student("Ravi")
t = Teacher("Math")
a = Admin()

s.show()
t.show()
a.manage()