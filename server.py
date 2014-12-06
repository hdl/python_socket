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
#create an inet, stream server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#bind the socket to host '' and port 7363
serverSocket.bind(('', 7363))
#server starts to listen to incoming TCP requests
serverSocket.listen(1)

#wait to accept a connection
connectionSocket, addr = serverSocket.accept()
while True:
    message = connectionSocket.recv(1024)
    connectionSocket.send("OK")
    print message

connectionSocket.close()
serverSocket.close() 

