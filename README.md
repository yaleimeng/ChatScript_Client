## [ChatScript](https://github.com/chatscriptnlp/ChatScriptNLP) python 客户端。

- 在客户端调用了结巴分词，这样服务器端不需要集成分词组件。大大减少了定制修改的工作量。
- Windows系统cmd窗口默认是GBK编码，即便自己修改成utf-8，仍有不少问题。干脆就用gbk编码发送给win下的服务器端。收到的信息采用utf-8解码。
- Linux服务器则比较简单，直接使用utf-8即可。如果是远程服务器，填入外网IP地址即可。

客户端图片：</br>
![客户端图片](https://github.com/yaleimeng/ChatScript_Client/blob/master/Pics/client.png)
Windows服务器端图片：</br>
![Windows服务器端](https://github.com/yaleimeng/ChatScript_Client/blob/master/Pics/server.png)
Linux服务器端图片：</br>
![Linux服务器端](https://github.com/yaleimeng/ChatScript_Client/blob/master/Pics/server_linux.png)
