from pony.orm import *
from datetime import date

_data_source_ = DataSource('sqlite', ':memory:', mapping='mapping1.xml')

class Group(Entity):
    number = PrimaryKey(int, auto=True)
    students = Set("Student")
    subjects = Set("Subject")

class Subject(Entity):
    name = PrimaryKey(str)
    groups = Set("Group")
    marks = Set("Mark")

class Person(Entity):
    first_name = Required(unicode)
    last_name = Required(unicode)
    passport = Optional(str)
    Unique(passport)

class Professor(Person):
    title = Required(str)

class Student(Person):
    group = Optional("Group")
    marks = Set("Mark")
    number = Unique(int, auto=True)

class Mark(Entity):
    student = Required("Student")
    subject = Required("Subject")
    PrimaryKey(student, subject)
    date = Required(date)
    value = Required(int)
