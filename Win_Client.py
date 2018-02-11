# Simple chat client to communicate with chat script server
# Not very efficient, since it uses a thread per socket model,
# If servicing a large number of clients, twisted may be a better fit

import jieba
import socket

# jieba.load_userdict("E:/ChatScript_8win/privatecode/Jieba/DICT/user.dict.utf8")  #使用自定义词典时需要预加载


def sendAndReceiveChatScript(msgToSend, server='127.0.0.1', port=1024, timeout=10):
    try:
        # Connect, send, receive and close socket. Connections are not persistent
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)  # timeout in secs
        s.connect((server, port))
        s.sendall(msgToSend)
        msg = ''            #定义了 标准字符串。
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
    server = "127.0.0.1"         # 本地服务器
    # server = "10.10.10.32"    # 如果是远程Windows服务器，填写您服务器的外网IP地址。
    #另外客户端ip必须在授权ip清单内，清单为all则允许所有ip访问。
    port = 1024
    botname = "Harry"
    user = "yalei"

    
    print("Hi " + user + ", enter ':quit' to end this session")

    while True:
        s = input("[" + user + "]" + ">> ").lower().strip()
        if s == ':quit':
            break
        # Ensure empty strings are padded with at least 1 space before sending to the
        # server, as per the required protocol

        if s[0]== ':' :     # 对于冒号开头的系统指令，原封不动发出去。
            mid = s
        elif s == "":       # 对于空的消息，变为1个空格发出去。
            mid =  " "
        else:               # 常规情况，做了分词然后发出去。
            seg_list = jieba.cut(s)
            mid = ' '.join(seg_list)   # 中间形态，分词后用空格隔开。
            print('分词后：',mid)
            
        # Send this to the server and print the response
        # Put in null terminations as required
        msg = '%s\u0000%s\u0000%s\u0000' % (user, botname, mid)
        msg = str.encode(msg,encoding='gbk')    #对消息使用GBK重新编码。否则，Windows版ChatScript无法正确响应

        resp = sendAndReceiveChatScript(msg, server=server, port=port)
        if resp is None:
            print("Error communicating with Chat Server")
            continue
            #break  # Stop on any error
        else:
            print("[Bot]: " + resp)
