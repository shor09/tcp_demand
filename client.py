#客户端
import socket
import struct
import json


class Client:
    def __init__(self, download_dir = 'D:/5EDemocache/', host = '127.0.0.1', port = 9090 ):
        self.download_dir = download_dir
        self.socket = None
        self.host = host
        self.port = port


    def create(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))


    def cmd(self):
        oo = self.socket.recv(4) # type: ignore
        data_size = struct.unpack("i", oo)[0]
        header_by = self.socket.recv(data_size) # type: ignore
        header_json = header_by.decode()
        header_dic = json.loads(header_json)
        body_size = header_dic["size"]

        recv_size = 0
        recv_data = b''
        a = [0]
        while recv_size < body_size:
            uco = self.socket.recv(1024) # type: ignore
            recv_data += uco
            recv_size += len(uco)
            a[0] += 1

        print(f"服务端返回：{recv_data.decode()}")
        print("success!"," ", f"共接收{a[0]}次")


    def download(self):
        oo = self.socket.recv(4) # type: ignore

        data_size = struct.unpack("i", oo)[0]

        header_by = self.socket.recv(data_size) # type: ignore

        header_json = header_by.decode()

        try:
            header_dic = json.loads(header_json)
        except Exception as e:
            print(e, " ", "文件不存在或文件无内容")
            return None

        print(f"服务端的报头为：{header_dic}")

        body_size = header_dic["size"]
        file_name = header_dic["file"]

        # recv_data = b''
        recv_size = 0
        a = [0]
        with open(r'%s/%s' % (self.download_dir, file_name), 'wb') as f:
            while recv_size < body_size:
                uco = self.socket.recv(1024)  # 接收信息，阻塞 # type: ignore
                f.write(uco)

                # recv_data += uco
                recv_size += len(uco)
                print(f"文件总大小为{body_size}，已下载{recv_size}")
                a[0] += 1

            print(f"接收了{a[0]}次")
            print("success!")
            return None


    def main(self):
        while True:
            data = input(">>>: ")
            if not data:
                continue
            self.socket.send(data.encode()) # type: ignore
            print("----发送成功----")
            if data == "exit":
                print("正在断开连接")
                break

            list1 = data.split(" ")
            if list1[0] == "get":
                self.download()
            else:
                self.cmd()

        self.socket.close() # type: ignore
        print("连接已断开")


if __name__ == '__main__':
    client = Client()
    client.create()
    client.main()