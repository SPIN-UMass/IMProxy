import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 3333))
s.listen(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1514)
        # if not data: break
        if len(data) > 0:
        	print (len(data))
        	