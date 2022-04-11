import unittest
from typing import Any

from jsonizer import Jsonizer
from jsonizer.exceptions import AmbiguityParamsException, UnparsedJsonException


class Person:
    def __init__(self, name: str, contacts: Any = None):
        self._name = name
        self._contacts = contacts

    def __str__(self) -> str:
        return f'Hi! I am {self._name}, my contacts are {self._contacts}'


class Worker:
    def __init__(self, name: str, income: int = 0):
        self._name = name
        self._income = income


class TestExceptions(unittest.TestCase):

    def test_ambiguity(self):
        with self.assertRaises(AmbiguityParamsException) as context:
            Jsonizer(Worker, Person)
        exception_message = str(context.exception)
        self.assertTrue(
            'Worker' in exception_message and 'Person' in exception_message,
            'Wrong classes names in exception message'
        )

    def test_ambiguity_fix(self):
        try:
            Jsonizer(Worker, Person, ignore_ambiguity=True)
        except AmbiguityParamsException:
            self.fail('Unexpected AmbiguityParamsException')

    def test_unparsed(self):
        person_data = {'name': 'Alice', 'contacts': {'phone': '123-456-7890'}}
        parser = Jsonizer(Person, disallow_dicts=True)
        with self.assertRaises(UnparsedJsonException) as context:
            parser.parse(person_data)
        exception_message = str(context.exception)
        self.assertTrue(
            '''"{'phone': '123-456-7890'}"''' in exception_message,
            'Wrong unparsed dict in exception message'
        )

    def test_unparsed_fix(self):
        person_data = {'name': 'Alice', 'contacts': {'phone': '123-456-7890'}}
        parser = Jsonizer(Person)
        try:
            person = parser.parse(person_data)
        except UnparsedJsonException:
            self.fail('Unexpected UnparsedJsonException')
        self.assertEqual(str(person), '''Hi! I am Alice, my contacts are {'phone': '123-456-7890'}''', 'Wrong parsing')
