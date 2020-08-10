import socket
import util


# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               


msg = s.recv()                                     

s.close()
print (msg.decode('ascii'))