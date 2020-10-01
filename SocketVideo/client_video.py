# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:28:33 2020

@author: ACER
"""
import socket
import cv2
import pickle
import struct

host = ""
port = 9999

s = socket.socket()
print("socket created")

s.connect(("192.168.1.10",port))

cap = cv2.VideoCapture(0)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret,frame = cap.read()
    res,frame = cv2.imencode('.jpg',frame,encode_param)
    data = pickle.dumps(frame,0)
    size = len(data)
    s.send(struct.pack(">L",size)+data)
    #server_msg = str(s.recv(1024),"utf-8")
    #print("Server message = "+str(server_msg))

cap.release()


