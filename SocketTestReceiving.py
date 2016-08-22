import socket

UDP_IP = "127.0.0.1"
# UDP_IP = "172.17.255.255"
UDP_PORT = 8100

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data


    #UDP
    #172.17.255.255
    #port: 8100