
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

class Meeting:
    def __init__(self, begin_time, duration, attendees):
        self.begin_time = begin_time
        self.duration = duration
        self.attendees_str = attendees
        self.attendees = []


class Oneday:
    def __init__(self,date):
        self.date = date
        self.meeting_list = []
