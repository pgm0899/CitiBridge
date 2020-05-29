# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
import pandas as pd


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

            ref_id1 = record[0]
            transRef = ref_id1[0:12]
            data['TID'].append(transRef)

            value_date = ref_id1[12:20]
            # value_date = value_date[:2] + '/' + value_date[2:4] + '/' + value_date[4:]
            data['DATE'].append(value_date)

            payerName = ref_id1[20:]
            data['PAYERNAME'].append(payerName)

            ref_id2 = record[1]
            payerAccNo = ref_id2[0:12]
            data['PAYERACC'].append(payerAccNo)

            payeeName = ref_id2[12:]
            data['PAYEENAME'].append(payeeName)

            ref_id3 = record[2]
            payeeAccNo = ref_id3[0:]
            data['PAYEEACC'].append(payeeAccNo)

            ref_id4 = record[3]
            amount = (ref_id4[0:])
            data['AMOUNT'].append(amount)

            # call validate functions
            status, reason = self.check_alphanumeric("transRef", transRef)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.date_validation(value_date)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.check_alphanumeric("payerName", payerName)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.check_alphanumeric("payerAccNo", payerAccNo)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.check_alphanumeric("payeeName", payeeName)
            if status == "Fail":
                data['STATUS'].append(status)
                data['REASON'].append(reason)
                continue
            status, reason = self.check_alphanumeric("payeeAccNo", payeeAccNo)
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

    def check_alphanumeric(self, str, data):
        if data.isalnum():
            return "Pass", "NA"
        else:
            return "Fail", str + " should be alpha-numeric string"

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
        return "Pass", "NA"

    def amt_validation(self, amount):
        amount = float(amount)
        round(amount, 2)
        if amount <= 0:
            return "Fail", "Transaction Amount is negative or 0"

        if amount >= 10 ** 10:
            return "Fail", "Transaction Amount should be less than 10 000 000 000.00"
        return "Pass", "NA"

# cf = ClearFeed()
# cf.validate()
