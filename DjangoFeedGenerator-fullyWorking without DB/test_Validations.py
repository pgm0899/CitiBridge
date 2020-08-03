# -*- coding: utf-8 -*-
import unittest 
#from Validations import check_alphanumeric
#from Validations import date_validation
#from Validations import amt_validation
import datetime

def check_alphanumeric(data):
    if data.isalnum():
        return 'Pass'
    else:
        return 'Fail'

def date_validation(date):
    try:
        datetime.datetime.strptime(date, '%d%m%Y')

    except ValueError:
        return "Fail"
    now = datetime.datetime.now()
    now_year = now.year
    y = date[4:]
    if y != str(now_year):
        return "Fail"
    return "Pass"

def amt_validation(amount):
    amount = float(amount)
    round(amount, 2)
    if amount <= 0:
        return "Fail"
    if amount >= 10 ** 10:
        return "Fail"
    return "Pass"

class MyTestCase(unittest.TestCase):

    def test0(self):
        self.assertEqual(check_alphanumeric('44Monica'), 'Pass')

    def test1(self):
        self.assertEqual(check_alphanumeric('Monica765'), 'Pass')

    def test2(self):
        self.assertEqual(check_alphanumeric('MonicaShetty123'), 'Pass')
    
    def test3(self):
        self.assertEqual(check_alphanumeric('Monica@123'), 'Fail')

    def test4(self):
        self.assertEqual(check_alphanumeric('Mona-)---'), 'Fail')

    def test5(self):
        self.assertEqual(check_alphanumeric(''), 'Fail')

    def test6(self):
        self.assertEqual(date_validation('01112020'), 'Pass')

    def test7(self):
        self.assertEqual(date_validation('29022020'), 'Pass')

    def test8(self):
        self.assertEqual(date_validation('05052018'), 'Fail')

    def test9(self):
        self.assertEqual(date_validation('02131999'), 'Fail')

    def test10(self):
        self.assertEqual(date_validation('021215'), 'Fail')

    def test11(self):
        self.assertEqual(date_validation(''), 'Fail')

    def test12(self):
        self.assertEqual(amt_validation('1234567890'), 'Pass')
        
    def test13(self):
        self.assertEqual(amt_validation('10'), 'Pass')
    
    def test14(self):
        self.assertEqual(amt_validation('125.50'), 'Pass')
    
    def test15(self):
        self.assertEqual(amt_validation('0'), 'Fail')
    
    def test16(self):
        self.assertEqual(amt_validation('-1000'), 'Fail')
    
    def test17(self):
        self.assertEqual(amt_validation('10000000000000'), 'Fail')
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
   


