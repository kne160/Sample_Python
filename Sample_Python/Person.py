'''
Sample Class

@author: kne16
'''

class Person():
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.name = name
        self.id = id

person = Person('I am a person')
student = Student('I am a student', 7)

print(person.name)
print(student.name, student.id)
