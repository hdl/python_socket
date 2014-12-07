# server code
'''
Beidou Yu
Due: 10/28/2014
Lab 4
Purpose: This server code maintains the schedule of a meeting room for the upcoming week. 
The TCPserver replies with the booking result. If the room is available within the requested time slot
 on the requested day, the room booking is recorded, 
 and a positive acknowledgement is returned to the user. 
 If the room is not available for the requested time slot on the requested day due to previous bookings, 
 no booking information is recorded, and a negative acknowledgement is returned to the user. 
 You should assume that the room is initially available for all hours in the upcoming week.

unique port number: 7363
'''

#import socket module
from socket import *
from common import *
import datetime
#create an inet, stream server socket
day_list=[]
user_db={}
def display_all(todo, connectionSocket, message):
    ack_str="ack#"
    for day in range(14):
        ack_str+=day_list[day].date+" scheduled slot: "
        for meeting in day_list[day].meeting_list:
            ack_str = ack_str + num2time(meeting.begin_time)+"-"+num2time(meeting.begin_time+meeting.duration)+"  "
        ack_str += '\n'
    print ack_str
    connectionSocket.send(ack_str)
def display_oneday(todo, connectionSocket, message):
    day = int(message.split('#')[1])
    ack_str="ack#"
    ack_str+=day_list[day].date+" scheduled slot: "
    for meeting in day_list[day].meeting_list:
        ack_str = ack_str + num2time(meeting.begin_time)+"-"+num2time(meeting.begin_time+meeting.duration)+"  "
    print ack_str
    connectionSocket.send(ack_str)
def display_upcoming(todo, connectionSocket, message):
    user_name = message.split("#")[1]
    ack_str=""
    for day in range(14):
        ack_str+=day_list[day].date+": "
        for meeting in day_list[day].meeting_list:
            for user in meeting.attendees:
                if user == user_name:
                    ack_str = ack_str + str(meeting.begin_time)+"-"+str(meeting.begin_time+meeting.duration)+"  "
        ack_str += '\n'
    print ack_str
    connectionSocket.send(ack_str)

def check_meeting(day, begin_time, duration):
    if begin_time !=0:
        if int(begin_time*10)%5 != 0:
            return "Begin time format wrong\n"
    if duration  == 0:
        return "Duration is zero\n"
    if int(duration*10)%5 !=0:
        return "Duration format wrong\n"
    for meeting in day_list[day].meeting_list:
        if meeting.begin_time<=begin_time<meeting.begin_time+duration:
            return "Time conflict(begin_time)\n"
        if meeting.begin_time<begin_time+duration<=meeting.begin_time+duration:
            return "Time conflict(duration)\n"
    return "OK"
def schd_meeting(todo, connectionSocket, message):
    day = int(message.split('#')[1])
    begin_time = float(message.split('#')[2])
    duration = float(message.split('#')[3])
    attendees = message.split('#')[4]
    reason = check_meeting(day, begin_time, duration)
    if reason == 'OK':
        day_list[day].meeting_list.append(Meeting(begin_time, duration, attendees))
    connectionSocket.send(reason)
def modify_meeting(todo, connectionSocket, message):
    day = int(message.split('#')[1])
    meeting = int(message.split('#')[2])
    begin_time = float(message.split('#')[3])
    duration = float(message.split('#')[4])
    attendees = message.split('#')[5]
    reason = check_meeting(day, begin_time, duration)
    if reason == 'OK':
        day_list[day].meeting_list[meeting].begin_time = begin_time
        day_list[day].meeting_list[meeting].duration=duration 
        day_list[day].meeting_list[meeting].attendees_str=attendees 
        day_list[day].meeting_list[meeting].update_attendees() 
    connectionSocket.send(reason)
def delete_meeting(todo, connectionSocket, message):
    day=int(message.split("#")[1])
    meeting=int(message.split("#")[2])
    if day<0 or day>=14:
        ack_str="Invalid day number"
    if meeting<0 or meeting>=len(day_list[day].meeting_list):
        ack_str="Invalid meeting number"
    else:
        del day_list[day].meeting_list[meeting]
        ack_str="OK"
    connectionSocket.send(ack_str)

todo_func = { 1: display_all,
              2: display_oneday,
              3: display_upcoming,
              4: schd_meeting,
              5: modify_meeting,
              6: delete_meeting,}

def init_day_list():
    for i in range(14):
        date_str = str(datetime.date.today() + datetime.timedelta(days=i))
        day_list.append(Oneday(date_str))
def main():
    init_day_list()
    user_db = get_user_info()
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    #bind the socket to host '' and port 7363
    serverSocket.bind(('', 7364))
    #server starts to listen to incoming TCP requests
    serverSocket.listen(1)
    print "Start listeng..."
    
    #wait to accept a connection
    connectionSocket, addr = serverSocket.accept()
    while True:
        message = connectionSocket.recv(1024)
        print "msg:"+message
        todo = int(message.split('#')[0])
        if todo == 0:
            break;
        todo_func[todo](todo, connectionSocket, message)
    
    connectionSocket.close()
    serverSocket.close() 

if __name__ == '__main__':
    main()

