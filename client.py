# client code
'''
Beidou Yu
Due: 10/28/2014
Lab 4 The client program is used by room users to request for the room before the upcoming week starts. 
Each request contains a desired time slot, and a day of week in the upcoming week.

'''

#import module
import sys, time
from socket import *
import datetime
from common import *
todo_g = 0
user_name_g =""

def display_all(todo, clientSocket):
    print todo
    clientSocket.send(str(todo))
    ack=clientSocket.recv(1024)
    print ack
def display_in_a_day(todo, clientSocket):
    print todo
    clientSocket.send(str(todo))
    ack=clientSocket.recv(1024)
    print ack
def display_upcoming(todo, clientSocket):
    print todo
    clientSocket.send(str(todo))
    ack=clientSocket.recv(1024)
    print ack
def schd_meeting(todo, clientSocket):
    print todo
    clientSocket.send(str(todo))
    ack=clientSocket.recv(1024)
    print ack
def modify_meeting(todo, clientSocket):
    print todo
    clientSocket.send(str(todo))
    ack=clientSocket.recv(1024)
    print ack
def delete_meeting(todo, clientSocket):
    print todo
    clientSocket.send(str(todo))
    ack=clientSocket.recv(1024)
    print ack

todo_func = { 1: display_all,
              2: display_in_a_day,
              3: display_upcoming,
              4: schd_meeting,
              5: modify_meeting,
              6: delete_meeting,}
def prompt_user_name():
    #read input to get user info
    user_db=get_user_info()
    user_name_list=[]
    user_name=''
    print("Please input your user name:")
    for key in user_db:
        print (key+" ("+user_db[key]+")")
        user_name_list.append(key)
    user_name = raw_input("User name only: ")
    while(user_name not in user_name_list):
        user_name = raw_input("Wrong Name, Try again, User name only: ")
    print ("Identity Confirmed. Welcome " + user_name)
    return user_name


#prompt user to select a function
def prompt_todo():
    while True:
        print "0: Quit"
        print "1: Display all the available slot"
        print "2: Display available slots in a specified day"
        print "4: Show upcoming schedules"
        print "3: Schedule a meeting"
        print "5: Modify a meeting"
        print "6: Delete a meeting"
        todo=input("Please select a functionality and hit Enter: ")
        if int(todo)<7 and int(todo)>0:
            return todo
        else:
            print("Invalid input number, try again")

def main():
    # Get the server hostname and port as command line arguments
    argv = sys.argv                      
    host = "127.0.0.1"
    port = "7363"
    
    print("This is a Room Booking App")
    user_name_g = prompt_user_name()

    #establish the connect
    try:
        print ("Begin connection")
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((host, int(port)))
        print "Done."
    except IOError:
        print("Timed out")

    #prompt user to select a functionality
    while True:
        todo = prompt_todo()
        if todo == 0:
            break
        else:
            todo_func[todo](todo, clientSocket)
    
    clientSocket.close()
    return 0
    
if __name__ == '__main__':
    main()