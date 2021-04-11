import socket
s = socket.socket()
print("Spcket Created...")
s.bind(('localhost',3030))
s.listen(3)
print("Waiting for Connection...")
while True:
    c,addr = s.accept()
    print("Connected with",addr)
    c.send ("welcome to  my world")
