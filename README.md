# basic-mail-merge
Here is a simple implementation of rudimentary mail merge functionality in Python.
This script was created to mail the details of WnCC’s Hello-FOSS initiative to many professors from IIT Bombay, IIT Hyderabad, IIT (ISM), IIM Kozhikode and IIM Amritsar.

It takes the names and emails of professors from the CSV files and uses Python’s excellent `smtplib` to send the mails based on the text in `template.txt`.
I have personally used this script to send emails to over 150 professors successfully.