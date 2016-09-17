# -*- coding: utf8 -*-
# Multi Thread
import socket
import traceback
import thread


def ReverseString(ss):
    ans = ''
    l = len(ss)
    while l > 0:
        l -= 1
        ans += ss[l]
    return ans

def ClientServer(clientsock, clientaddr):
    try:
        print(clientsock.getpeername())
        while 1:
            data = clientsock.recv(1024)
            if not len(data):
                break
            print(clientsock.getpeername()),
            print(': '+str(data))
            back = ReverseString(str(data))
            clientsock.sendall(back + "\n")
            # clientsock.sendall("\nI get it!\n")

    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()

def main():
    host = ''
    port = 3333
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    while 1:
        try:
            clientsock, clientaddr=s.accept()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue
        thread.start_new_thread(ClientServer, (clientsock, clientaddr))

if __name__ == "__main__":
  main()