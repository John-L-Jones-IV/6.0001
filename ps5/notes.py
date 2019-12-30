#!/usr/bin/env python3
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age = newage
    def set_name(self, newname=''):
        self.name = newname
    def __str__(self):
        return 'animal:'+str(self.name)+":"+str(self.age)
    # getters and setters should be used outside of a class
    # this is the idea of information hiding, you want to abstract some data

class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return 'cat:'+str(self.name)+':'+str(self.age)

class Person(Animal):
    num_people = 0
    def __init__(self,age,name,friends=[]):
        Animal.__init__(self,age)
        self.name = name
        self.friends = friends
        num_people += 1
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self,other):
        diff = abs(self.age - other.age)
        print(diff, 'year difference')
    def __str__(self):
        return 'person:'+str(self.name)+':'+str(self.age)
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print('I have homework')
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r < 0.75:
            print('I should eat')
        else:
            print('I am watching TV')
    def __str__(self):
        return 'student:'+str(self.name)+':'+str(self.age)+':'+str(self.major)


if __name__ == '__main__':
    wife = Person(25,'Liz', ['Husband', 'Sister', 'Sally'])
    print(wife.get_friends())
    me = Student('John', 24, 'EE')
    me.speak()
    print(People.num_people)
