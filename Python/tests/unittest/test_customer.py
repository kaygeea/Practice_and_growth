#!/usr/bin/python3
'''This module tests the Customer class with unittest'''


import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    '''This class implements unittest testing for Customer class'''

    def setUp(self):
        '''This method defines a customer() instance'''
        self.customer_1 = Customer('John', 'Brad', 5000)
        self.customer_2 = Customer('Tina', 'Smith', 3000)

    def test_customer_mail(self):
        '''This method creates a test for the customer.customer_mail method'''
        self.assertEqual(self.customer_1.customer_mail, 'John.Brad@email.com')
        self.assertEqual(self.customer_2.customer_mail, 'Tina.Smith@email.com')

    def test_customer_fullname(self):
        '''This method creates a test for customer.customer_fullname method'''
        self.assertEqual(self.customer_1.customer_fullname, 'John Brad')
        self.assertEqual(self.customer_2.customer_fullname, 'Tina Smith')

    def test_apply_discount(self):
        '''This method creates a test for customer.apply_discount method'''
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()

        self.assertEqual(self.customer_1.purchase, 4750)
        self.assertEqual(self.customer_2.purchase, 2850)

if __name__ == '__main__':
    unittest.main()
