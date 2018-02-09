# Simple chat client to communicate with chat script server
# Not very efficient, since it uses a thread per socket model,
# If servicing a large number of clients, twisted may be a better fit

from optparse import OptionParser
import jieba
import socket
import sys
jieba.load_userdict("E:/ChatScript_8win/privatecode/Jieba/DICT/user.dict.utf8")


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
    server = "127.0.0.1"            # 本地服务器

    # server = "10.28.108.32"        # 连接MOA服务器，不成功。暂时不考虑
    #server = '118.178.192.184'
    port = 1024
    botname = "Harry"
    user = "yalei"

    # Setup the command line arguments.
    optp = OptionParser()

    # user name to login to chat script as
    optp.add_option("-u", dest="user", help="user id, required")
    # botname
    optp.add_option("-b", dest="botname", help="which bot to talk to, if not specified, will use default bot")
    # server
    optp.add_option("-s", dest="server", help="chat server host name (default is " + str(server) + ")")
    # port
    optp.add_option("-p", dest="port", help="chat server listen port (default is " + str(port) + ")")

    opts, args = optp.parse_args()

    # if opts.user is None:
    #     optp.print_help()
    #     sys.exit(1)
    # user = opts.user
    botname = opts.botname if opts.botname is not None else botname
    server = opts.server if opts.server is not None else server
    port = int(opts.port) if opts.port is not None else port

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
            mid = s

        print(mid)
        # Send this to the server and print the response
        # Put in null terminations as required
        msg = '%s\u0000%s\u0000%s\u0000' % (user, botname, mid)
        msg = str.encode(msg,encoding='gbk')

        resp = sendAndReceiveChatScript(msg, server=server, port=port)
        if resp is None:
            print("Error communicating with Chat Server")
            continue
            #break  # Stop on any error
        else:
            print("[Bot]: " + resp)