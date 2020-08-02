# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
import pandas as pd
import shutil
from sqlalchemy import create_engine


database_username = 'root'
database_password = 'Niki@0511'
database_name = 'citi'
# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user=database_username,
                               pw=database_password,
                               db=database_name))

class ClearFeed:

    def __init__(self):
        pass

    def validate(self):
        f = open('static/upload.txt', 'r')
        data = {'TID': [],
                'DATE': [],
                'PAYERNAME': [],
                'PAYERACC': [],
                'PAYEENAME': [],
                'PAYEEACC': [],
                'AMOUNT': [],
                'STATUS': [],
                'REASON': []
                }

        while True:
            line = f.readline()
            if not line:
                # write df to file
                df = pd.DataFrame(data)
                print(df)
                print('dataframe')
                df.to_csv(r'static/all.csv', index=False, header=True)
                '''outfile = open('static/all.csv', 'w')'''
                break

            record = line.split()

            flag = 0
            if len(record) >= 1:
                ref_id1 = record[0]

                if len(ref_id1) >= 12:
                    transRef = ref_id1[0:12]
                    data['TID'].append(transRef)
                else:
                    data['TID'].append("InvalidEntry")
                    flag = 1

                if len(ref_id1) >= 20:
                    value_date = ref_id1[12:20]
                    data['DATE'].append(value_date)
                else:
                    data['DATE'].append("InvalidEntry")
                    flag = 1

                if len(ref_id1) > 20:
                    payerName = ref_id1[20:]
                    data['PAYERNAME'].append(payerName)
                else:
                    data['PAYERNAME'].append("InvalidEntry")
                    flag = 1
            else:
                data['TID'].append("InvalidEntry")
                data['DATE'].append("InvalidEntry")
                data['PAYERNAME'].append("InvalidEntry")
                flag = 1

            if len(record) >= 2:
                ref_id2 = record[1]
                if len(ref_id2) >= 12:
                    payerAccNo = ref_id2[0:12]
                    data['PAYERACC'].append(payerAccNo)
                else:
                    data['PAYERACC'].append("InvalidEntry")
                    flag = 1

                if len(ref_id2) > 12:
                    payeeName = ref_id2[12:]
                    data['PAYEENAME'].append(payeeName)
                else:
                    data['PAYEENAME'].append("InvalidEntry")
                    flag = 1
            else:
                data['PAYERACC'].append("InvalidEntry")
                data['PAYEENAME'].append("InvalidEntry")
                flag = 1

            if len(record) >= 3:
                ref_id3 = record[2]
                if len(ref_id3) > 0:
                    payeeAccNo = ref_id3[0:]
                    data['PAYEEACC'].append(payeeAccNo)
                else:
                    data['PAYEEACC'].append("InvalidEntry")
                    flag = 1
            else:
                data['PAYEEACC'].append("InvalidEntry")
                flag = 1

            if len(record) == 4:
                ref_id4 = record[3]
                if len(ref_id4) > 0:
                    amount = (ref_id4[0:])
                    data['AMOUNT'].append(amount)
                else:
                    data['AMOUNT'].append("InvalidEntry")
                    flag = 1
            else:
                data['AMOUNT'].append("InvalidEntry")
                flag = 1

            if flag == 1:
                data['STATUS'].append("Fail")
                data['REASON'].append("Invalid number of entries")
                continue

            # call validate functions
            status, reason = self.check_alphanumeric12("transRef", transRef)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.date_validation(value_date)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.check_name("payerName", payerName)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.check_alphanumeric12("payerAccNo", payerAccNo)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.check_name("payeeName", payeeName)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.check_alphanumeric12("payeeAccNo", payeeAccNo)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.amt_validation(amount)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue

            data['STATUS'].append(status)
            data['REASON'].append(reason)

    def check_alphanumeric12(self, str1, data):
        if len(data) != 12:
            return "Fail", str1 + " should be a alpha-numeric string of length 12"

        if data.isalnum():
            return "Pass", "All fields are valid"
        else:
            return "Fail", str1 + " should be alpha-numeric string"

    def check_name(self, str1, data):
        if len(data)>35:
            return "Fail", str1 + " should be alphabetical string of maximum length 35"
        if data.isalpha():
            return "Pass", "All fields are valid"
        else:
            return "Fail", str1 + " should be alphabetical string"

    def date_validation(self, date):
        try:
            datetime.datetime.strptime(date, '%d%m%Y')

        except ValueError:
            return "Fail", "Incorrect date format(should be DDMMYYYY)"

        now = datetime.datetime.now()
        now_year = now.year
        y = date[4:]
        if y != str(now_year):
            return "Fail", "Incorrect year"
        return "Pass", "All fields are valid"

    def amt_validation(self, amount):
        amt = amount.split('.')
        if len(amt) > 2:
            return "Fail", "Transaction Amount should be a float with maximum 2 digits after decimal"
        if not all([i.isnumeric() for i in amt]):
            return "Fail", "Transaction Amount should be numeric"

        amount = float(amount)
        round(amount, 2)
        if amount <= 0:
            return "Fail", "Transaction Amount is negative or 0"

        if amount >= 10 ** 10:
            return "Fail", "Transaction Amount should be less than 10 000 000 000.00"
        return "Pass", "All fields are valid"

# cf = ClearFeed()
# cf.validate()

