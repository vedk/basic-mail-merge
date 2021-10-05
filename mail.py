import sys
import csv
import smtplib, ssl

port = 587  # For starttls
smtp_server = 'smtp-auth.iitb.ac.in'
sender_email = 'student@iitb.ac.in'
password = 'password'

rec_emails = list()
template = str()
msgs = list()


with open('template.txt', 'r') as fd:
    template = fd.read()

with open('your_file.csv', 'r') as data:
    reader = csv.reader(data)

    index = 0
    for row in reader:
        rec_emails.append(row[1])
        msgs.append(template % (sender_email, row[1], row[0], row[2]))
        with open('emails/email_' + str(index) + '.txt', 'w') as outfd:
            outfd.write(msgs[index])

        index += 1


if sys.argv[1] == 's':

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        try:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)

            for index in range(len(rec_emails)):
                server.sendmail(sender_email, rec_emails[index], msgs[index])
                print('Sent email ' + str(index))
        except Exception as ex:
            print(ex)