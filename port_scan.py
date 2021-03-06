import socket
import sys

def scan(host, timer):
    if len(sys.argv) > 4:
        ports = range(int(sys.argv[2]), int(sys.argv[3]))
        t = sys.argv[4]

        if t == "t1":
            timer = 0.1
        elif t == "t2":
            timer = 0.4
        elif t == "t3":
            timer = 0.7
        elif t == "t4":
            timer = 1
        else:
            timer = 2

    elif len(sys.argv) > 3:
        ports = range(int(sys.argv[2]), int(sys.argv[3]))

    else:
        ports = range(1, 3307)


    print(" PORTA | STATUS")

    for porta in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timer)

        code = client.connect_ex((host, porta))

        if code == 0:
            print(f' {porta}/tcp | OPEN')


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        ports = 0
        timer = 1
        scan(host, timer)
    else:
        print("Usage: python3 host")
        print("or")
        print("Usage: python3 host starting_port end_port timer")
