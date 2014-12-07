
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
    def __init__(self):
        self.begin_time = 0
        self.duration = 0
        self.attendees = []

class Oneday:
    def __init__(self,date):
        self.date = date
        self.meeting_list = []
