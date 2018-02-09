# Simple chat client to communicate with chat script server
# Not very efficient, since it uses a thread per socket model,
# If servicing a large number of clients, twisted may be a better fit

import jieba
import socket

jieba.load_userdict("D:/jieba5/DICT/user.dict.utf8")


def sendAndReceiveChatScript(msgToSend, server='127.0.0.1', port=1024, timeout=10):
    try:
        # Connect, send, receive and close socket. Connections are not persistent
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)  # timeout in secs
        s.connect((server, port))
        s.sendall(msgToSend)
        msg = ''  # 定义了 标准字符串。
        while True:
            chunk = s.recv(1024)
            if chunk == b'':
                break
            msg += chunk.decode("utf-8")
        s.close()
        return msg
    except:
        return None


if __name__ == '__main__':
    server = '118.178.192.184'  # 服务器的外网IP地址。另外客户端ip在授权ip清单内，清单为all则允许所有ip访问。
    port = 1024                 # 默认端口为1024
    botname = "Harry"           # 默认Bot为Harry
    user = "yalei"              # 用户名可以自己指定

    print("你好 " + user + "。 如需结束会话，请输入 ':quit'。")

    while True:
        s = input("[" + user + "]" + ">> ").lower().strip()
        if s == ':quit':
            break
        elif s[0] == ':':  # 对于冒号开头的系统指令，原封不动发出去。
            mid = s
        elif s == "":  # 按照通信协议要求，对于空的消息，变为1个空格发出去。
            mid = " "
        else:  # 常规情况，做了分词然后发出去。
            seg_list = jieba.cut(s)
            mid = ' '.join(seg_list)  # 中间形态，分词后用空格隔开。
            print('分词后：', mid)

        # Send this to the server and print the response。   Put in null terminations as required
        msg = '%s\u0000%s\u0000%s\u0000' % (user, botname, mid)
        resp = sendAndReceiveChatScript(str.encode(msg), server=server, port=port)
        if resp is None:
            print("Error communicating with Chat Server")
            continue  # 忽略所有错误。如果遇到错误要退出程序，则使用  break  语句。
        else:
            print("[Bot]: " + resp)