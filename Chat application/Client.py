import socket

HEADER = 10
PORT = 1234 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!USER DISCONNECT!"
IP=socket.gethostbyname(socket.gethostname()) 
ADDR = (IP, PORT) 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
NAME = input("Enter Name: ")
client.send(NAME.encode(FORMAT))
instruct=""
status_update=""

def send_server(msg):
    global status_update
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_len = str(msg_length).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    if msg!=DISCONNECT_MESSAGE:
        data=client.recv(1024).decode()
    if status_update=="END":
        print("!DISCONNECTED FROM SERVER!")
        return
    status_update=data
    if msg!=DISCONNECT_MESSAGE and status_update!="END":
        print(f"[ADMIN]: {data}")

print("Connected to server")
while True:
    if status_update=="END":
        break
    instruct=input("[You]: ")
    if instruct=="QUIT":
        status_update="END"
        break
    else:
        send_server(instruct)
send_server(DISCONNECT_MESSAGE)
client.close()
