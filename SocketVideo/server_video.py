# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:53:46 2020

@author: ACER
"""

import socket
import pickle
import struct
import numpy as np
import cv2

host = ""
port = 9999
s=socket.socket()
print('Socket created')

s.bind((host,port))
print('Socket bind complete')
s.listen(5)
print('Socket now listening')

conn,addr=s.accept()
print("Connection with: IP-"+str(addr[0])+" Port-"+str(addr[1]))
s.setblocking(1)

data = b""
rec_size = struct.calcsize(">L")
while True:
    while(len(data)<rec_size):
        data+=conn.recv(4096)
    print("Started receiving data")
    inp_msg_size = data[:rec_size]
    data = data[rec_size:]
    msg_size = struct.unpack(">L",inp_msg_size)[0]
    while(len(data)<msg_size):
        data+= conn.recv(4096)
    fr_data = data[:msg_size]
    data = data[msg_size:]
    
    frame = pickle.loads(fr_data,fix_imports = True,encoding = "bytes")
    frame = cv2.imdecode(frame,cv2.IMREAD_COLOR)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

conn.close()
s.close()
cv2.destroyAllWindows()