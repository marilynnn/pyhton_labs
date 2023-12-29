from aiohttp import web
import json
import datetime


class Lab:
    '''Класс лабораторной работы'''
    def __init__(self, name, date):
        self.name = name  # название лабораторной
        self.date = datetime.datetime.strptime(date, '%d.%m.%Y')  # дата сдачи
        self.descr = None  # описание лабораторной (опционально)
        self.students = []  # список студентов, сдавших данную лабораторную работу (опционально)

    def set_descr(self, descr):
        self.descr = descr

    def add_students(self, students):
        if hasattr(students, '__iter__'):
            self.students.extend(students)
        else:
            self.students.append(students)

