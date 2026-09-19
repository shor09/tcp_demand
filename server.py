#服务端
from socket import * # type: ignore
import os
import socket
import subprocess
import struct
import json
import threading

class Server:
    def __init__(self, host='127.0.0.1', port=9090, share_dir="D:/5EDemocache/1.jpg"): # 路径自由更换
        self.host = host
        self.port = port
        self.share_dir = share_dir
        self.socket = None
        self.client = None
        self.client_addr = None


    def create(self):
        self.socket = socket.socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)


    @staticmethod
    def cmd(sli, ccc):
        obj = subprocess.Popen(ccc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # 执行客户端传入的命令
        obj.wait()
        cro = obj.stdout.read() # type: ignore
        err = obj.stderr.read() # type: ignore

        header_dict = {
            "size": len(cro) + len(err)
        }

        header_by = json.dumps(header_dict).encode()
        header = struct.pack("i", len(header_by))

        sli.sendall(header)
        sli.sendall(header_by)
        sli.sendall(cro)
        sli.sendall(err)
        print("发送成功")


    def get(self, sli, list1):
        filename = list1[1]
        # 制作报头

        header_dict = {
            "file": filename,
            "size": os.path.getsize(os.path.join(self.share_dir, filename))
        }

        header_by = json.dumps(header_dict).encode()
        header = struct.pack("i", len(header_by))

        # 发送
        sli.send(header)
        sli.send(header_by)

        # 读取文件内容并发送
        with open(os.path.join(self.share_dir, filename), 'rb') as f:
            for by in f:
                sli.sendall(by)

        print("发送成功")


    def run_cli(self, client_socket, client_addr):
        print(f"客户端已连接，来自{client_addr}")
        while True:
            try:
                ccc = client_socket.recv(1024).decode()
                if not ccc:
                    print("客户端强制断开")
                    break
                print(f"收到客户端信息：{ccc}")
                if ccc == "exit":
                    print(f"客户端{client_addr}主动断开，断开中。。。")
                    break
            except Exception as e:
                print(e)
                print("客户端强制断开")
                break

            list1 = ccc.split(" ")

            acc = list1[0]
            if acc == "get":
                self.get(client_socket, list1)
            else:
                self.cmd(client_socket, ccc)

        client_socket.close()
        print("断开成功")



    def main(self):
        while True:
            client_socket, client_addr = self.socket.accept() # type: ignore
            #建立线程
            client_threads = threading.Thread(target =self.run_cli, args = (client_socket, client_addr))
            client_threads.start()



if __name__ == '__main__':
    server = Server()
    server.create()
    server.main()