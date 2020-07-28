Clearing Feed Generation is a web application system that generates a feed file towards a clearing system in a specific format based on the input transactions to the system.
The functional model for this project is to maintain a traversing workflow of uploading an input file which is a system generated trasaction file,which will be validated 
for a transaction to pass or fail and further be archived as feed generated.
A local folder is polled to pick up a transaction file on which validations are performed such as number of fields within a record,field length,date format and currency format
once the file is validated and cleared the generated feed is archived
Following fields are validated :Transaction reference number,Value date, Name and Account number of the Payer and Payee, amount.

This project is done using django framework and the backend code for validation is written in python and data is stored using mysql database,the UI screen which shows all the transactions is written in html,css and bootstrap.
A login functionality is provided for a user to login and upload a file for clearing.
For a failed transaction the reason for validation failure is also displayed on the UI screen.

The templates and static folder consists of the UI code written for login page,input file page and transactions validated page
The takeinput folder consists of the clearfeedbackendcode.py file that is the backend code for validation
The archivedata file within the static folder consists of the files that are cleared/validated and archived.


