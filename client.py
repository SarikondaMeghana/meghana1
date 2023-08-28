import time, socket, sys
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    host_Cisco = config['cisco']['host_Cisco']
    port_Cisco = config['cisco']['port_Cisco']
    host_HCL = config['HCL']['host_HCL']
    port_HCL = config['HCL']['port_HCL']
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
s = socket.socket()
s1 = socket.socket()
name = input(str("\nEnter your name: "))


def main():
    sockethost()
    socketconn()
    receiver()


def sockethost():
    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)
    print(shost, "(", ip, ")\n")
    print("\nTrying to connect to ", host_Cisco, "(", port_Cisco, ")\n")
    print("\nTrying to connect to ", host_HCL, "(", port_HCL, ")\n")
    time.sleep(1)


def socketconn():
    global s_name
    global s1_name
    try:
        s.connect((host_Cisco, port_Cisco))
        s1.connect((host_HCL, port_HCL))
    except:
        print("Unable to connected to servers")
    finally:
        print("Connected to servers...\n")
    s.send(name.encode())
    s_name = s.recv(config['byte'])
    s_name = s_name.decode()
    s1.send(name.encode())
    s1_name = s1.recv(config['byte'])
    s1_name = s1_name.decode()
    print(s_name, "has joined the chat room\ngive exit to exit chat room\n")
    print(s1_name, "has joined the chat room\nEnter exit to exit chat room\n")


def receiver():
    while True:
        message = s.recv(config['byte'])
        message = message.decode()
        message1 = s1.recv(config['byte'])
        message1 = message1.decode()
        print(s_name, ":", message)
        print(s1_name, ":", message1)
        message = input(str("You : "))
        if message == "exit":
            message = "Left chat room!"
            s.send(message.encode())
            print("\n")
            s1.send(message1.encode())
            print("\n")
            break
        s.send(message.encode())
        s1.send(message.encode())


if __name__ == "__main__":
    main()

