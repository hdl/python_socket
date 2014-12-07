import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def get_user_info():
    user_db={}
    file = open("input.txt")
    while True:
        line = file.readline()
        if not line:
            break
        key = line.split()[0]
        value = line.split()[1]
        user_db[key]=value;
    file.close()
    return user_db
def num2time(number):
    number_str=str(number)
    if '.' in number_str:
        h = number_str.split('.')[0]
        minute = number_str.split(".")[1]
        if minute=='0':
            h+=":00"
        if minute == '5':
            h+=":30"
    else:
        h = number_str.split('.')[0]+":00"
    return h

class Meeting:
    def __init__(self, begin_time, duration, attendees):
        self.begin_time = begin_time
        self.duration = duration
        self.attendees_str = attendees
        self.attendees = attendees.split()
        self.send_email()
        print self.attendees
    def update_attendees(self):
        self.attendees = attendees.split()
    def send_email(self):
        user_db = get_user_info()
        for name in self.attendees:
            if user_db[name]:
                you = user_db[name]


class Oneday:
    def __init__(self,date):
        self.date = date
        self.meeting_list = []
