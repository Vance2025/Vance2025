class Student():
    sum1 = 0
    name = '123'
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.age)
        print(name)
        print(Student.sum1)
        print(self.__class__.sum1)

    def do_homework(self):
        print('homework is done')

    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)
        print(cls.__name__)

student1 = Student('Vance', 18)
print(student1.name)
print(student1.age)
student1.do_homework()
student2 = Student('Alice', 20)
print(student2.age)
print(student2.name)
student3 = Student('Bob', 22)

print(Student.plus_sum())

