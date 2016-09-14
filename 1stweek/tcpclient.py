# -*- coding: utf8 -*-

import socket,sys

def main():
    port = 3333
    host = '127.0.0.1'
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except:
        print('连接错误！')
    # s.send(data)
    # s.shutdown(1)
    print('发送完成。')
    while 1:
        data = raw_input('输入要发送的信息：')

        s.send(data)

        buf=s.recv(4096)
        if not len(buf):
            break
        sys.stdout.write(buf)

if __name__ == "__main__":
  main()