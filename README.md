# tcp_demand

一个基于 Python Socket 的简单 TCP 文件传输项目。

## 项目简介

这是一个用于学习 Python 网络编程和 TCP Socket 通信的练习项目。

目前实现了客户端（Client）和服务端（Server）之间的基本通信以及单个指定文件传输功能，以及简易终端。

服务端可以建立多个对客户端的连接，客户端目前只能建立一个连接。

会持续更新优化

## 项目结构

```text
tcp_demand/
├── client.py       # 客户端
├── server.py       # 服务端
└── README.md       # 项目说明
```

## 环境

* Python 3.x
* TCP Socket
* 推荐Windows，暂未测试其他操作系统运行情况

## 使用方法

### 1. 启动服务端

运行：

```bash
python server.py
```

### 2. 启动客户端

打开另一个终端，运行：

```bash
python client.py
```

目前并没有专门的详细使用说明，需自行查看代码（以后的版本会添加）。

## 学习

通过这个项目可以学习：

* Python Socket 编程
* TCP 客户端 / 服务端模型
* 网络数据传输
* 文件传输
* Python 网络编程中的数据处理

## 注意

该项目的简易终端功能目前存在风险漏洞，可能会被利用，谨慎使用，或者可以直接删除相关代码。


## License

This project is for learning and personal use.
