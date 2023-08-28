import time, socket, sys
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
s = socket.socket()
time.sleep(1)
host = config['cisco']['host_Cisco']
port = config['cisco']['port_Cisco']


def main():
    server()
    exceptionHandle()


def server():
    global conn, addr
    global s_name
    name = input(str("Enter your name: "))
    s.bind((host, port))
    s.listen(1)
    print("\nWaiting for incoming connections...\n")
    conn, addr = s.accept()
    print("Received connection from ", addr[0], "(", addr[1], ")\n")
    s_name = conn.recv(config['byte'])
    s_name = s_name.decode()
    print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
    conn.send(name.encode())


def exceptionHandle():
    while True:
        message = input(str("You : "))
        try:
            if message == "exit":
                message = "Left chat room!"
                conn.send(message.encode())
                print("\n")
                break
            conn.send(message.encode())
            message = conn.recv(config['byte'])
            message = message.decode()
            print(s_name, ":", message)
        except ConnectionAbortedError:
            print('Client has left the chat')


if __name__ == "__main__":
    main()

