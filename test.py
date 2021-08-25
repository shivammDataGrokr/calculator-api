import unittest
from flask import requests


class TestCalc(unittest.TestCase):
    URL = 'http://127.0.0.1:5000/calculator'


    def test_addition(self):
        Url = "{}/addition".format(TestCalc.URL)
        response = requests.post(Url, json={'num1': 77, 'num2': -7})
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        self.assertEqual(result, 70)

    def test_subtraction(self):
        Url = "{}/subtraction".format(TestCalc.URL)
        response = requests.post(Url, json={'num1': 7, 'num2': 7})
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        self.assertEqual(result, 0)

    
    def test_multiplication(self):
        Url = "{}/multiplication".format(TestCalc.URL)
        response = requests.post(Url, json={'num1': 77, 'num2': 7})
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        self.assertEqual(result, 539)

    def test_division(self):
        Url = "{}/division".format(TestCalc.URL)
        response = requests.post(Url, json={'num1': 77, 'num2': 7})
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        self.assertEqual(result, 11)


if __name__ == "__main__":
    tester = TestCalc

    tester.test_addition
    tester.test_subtraction
    tester.test_multiplication
    tester.test_division
