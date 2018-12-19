# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/18


# 1.什么是C/S架构？
# server/client架构

# 2.互联网协议是什么？分别介绍五层协议中每一层的功能？
# 计算机通信定义的规范。
# 应用层   应用程序告诉操作系统，要给某ip port 发送bytes数据
# 传输层   建立端口到端口的通信
# 网络层   引入一套新的地址用来区分不同的广播域／子网，这套地址即网络地址
# 数据链路层 单纯的电信号0和1没有任何意义，定义了电信号的分组方式，将网络层传过来的数据进行分组
# 一组电信号构成一个数据包，叫做‘帧’每一数据帧分成：报头head和数据data两部分
# 物理层   将链路层传过来的数据用高低压的电流传输

# 3.基于tcp协议通信，为何建立链接需要三次握手，而断开链接却需要四次挥手
# A请求和B建立链接
# 1.A发送请求建立链接信息给B，syn=1&seq=X
# 2.B收到syn=1&seq=X，发送确认建立链接信息和请求建立链接信息，syn=1&ack=X+1&seq=Y
# 3.A接到syn=1&ack=X+1&seq=Y后，发送确认建立链接信息给B ack=Y+1&seq=Z
# A请求和B断开链接
# 1.A发送请求断开链接信息给B，fin=1&seq=X
# 2.B收到fin=1&seq=X，发送确认断开链接信息ack=1&seq=X+1
# 3.B发送确认断开链接信息fin=1&seq=Y
# 3.A接到fin=1&seq=Y后，发送确认断开链接信息给B ack=Y+1&seq=Z
# 建立链接和断开链接的过程是一样的，只是被建立链接方把第二步的确认建立链接和第三步发送建立链接信息合并了
# 之所以断开链接有四次，是因为B不确定什么时候断开链接，也许A在发送断开请求的时候，B还有数据正在发送给A，此时可单方面断开A到B，还不能断开B到A

# 4.为何基于tcp协议的通信比基于udp协议的通信更可靠？
# 因为tcp会有确认动作，如果对方没接收到，会再次发送，直到收到对方确认信息为止

# ‍5.流式协议指的是什么协议，数据报协议指的是什么协议？
# 流式协议：数据像水流一样，源源不断传输，发送端和接收端都可以实时接收一定字节大小的数据
# 数据包协议(upd)：一次发送就是一个数据包，不存在源源不断的发送，发送端和接收端都只能一个个包的接收，不能接收指定长度大小的数据

# 6.什么是socket？简述基于tcp协议的套接字通信流程
# socket：一组接口，作用于应用程序于传输层之间，等于是将传输层做了一次封装，用户只要和socket简单交互，复杂的事情交给socket与传输层交互
# 通信流程：服务端：生成socket对象->绑定ip port->监听客户端链接->建立链接->收发数据
#         客户端：生成socket对象->链接ip port->建立链接->收发数据
#
# 7.什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？
# 粘包：将多次发送的数据粘到一起，致使接收方无法区分数据包
# 原因：1.发送方，有发送算法机制，会将短期内且数据包不大，会将多个包打成一个包进行发送
#      2.接收方，当一次接收字节小于包的大小时，未接收完的数据会存留在系统内存中，下次有数据包过来时会粘在一起
# 解决方法：每次发送数据包之前，告诉接收方此次发送的数据包的大小，接收方根据包大小接收指定长度的数据

# 8.基于socket开发一个聊天程序，实现两端互相发送和接收消息
# 略，作业可比这个难太多

# 9.基于tcp socket，开发简单的远程命令执行程序，允许用户执行命令，并返回结果
# 略，已实现

# 10.基于tcp协议编写简单FTP程序，实现上传、下载文件功能，并解决粘包问题
# 略，已实现

# 11.基于udp协议编写程序，实现功能
# 执行指定的命令，让客户端可以查看服务端的时间
# 执行指定的命令，让客户端可以与服务的的时间同步
# 略
