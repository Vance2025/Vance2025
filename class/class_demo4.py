
from class_demo5 import People

class Student(People):
    sum1 = 0

    def __init__(self, school, name, age):
        self.school = school
        super(Student,self).__init__(name, age)

        # self.score = 0


    def do_homework(self):
        super(Student, self).hacer_tarea()

    def marking(self, score):
        if score < 0:
            return 'Error! The score cannot be negative.Please re-enter the score.'
        self.score = score
        print(self.name + ' score is:' + str(self.score))


    # @classmethod
    # def plus_sum(cls):
    #     cls.sum1 += 1
    #     print(cls.sum1)

    # @staticmethod
    # def add(x, y):
    #     print('This is a static method')
    #     print(Student.sum1)
    #     print('sum is:', x+y)

student1 = Student('College','Vance', 18)
# print(student1.sum)
# print(Student.sum)
print(student1.get_name())
print(student1.name)
print(student1.age)
print(student1.school)
student1.do_homework()



# student2 = Student('Alice', 20)
# student3 = Student('Bob', 22)

# print(Student.plus_sum())
# print(Student.plus_sum())  

# student1.add(1, 2)
# Student.add(1, 2)