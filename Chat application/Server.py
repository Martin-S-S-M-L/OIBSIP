import socket
import threading

HEADER=10
IP=socket.gethostbyname(socket.gethostname()) 
PORT=1234 
ADDR=(IP, PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE = "!USER DISCONNECT!"
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
instruct=""

def handle_client(connect,addr):
    NAME = connect.recv(1024).decode(FORMAT)
    print(f"\n{NAME} has connected.\n")
    conn = True
    while conn:
        msg_length = connect.recv(HEADER).decode(FORMAT) 
        if msg_length:
            msg_length = int(msg_length)
            msg = connect.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                conn=False
            print(f"[{NAME}] {msg}")
            if msg!=DISCONNECT_MESSAGE:
                instruct=input("[YOU]: ")
                connect.send(instruct.encode())
            if instruct=="END":
                print("!DISCONNECTED!")
                break
    connect.close()

def start():
    server.listen()
    print(f"Listening Server...")
    while True:
        connect,addr = server.accept()
        thread= threading.Thread(target= handle_client, args=(connect,addr))
        thread.start()
        print(f" Active Connection {threading.active_count()-2}")

print("Starting Server...")
start()
