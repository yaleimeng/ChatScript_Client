# ChatScript_Client
ChatScript python 客户端。

- 在客户端调用了结巴分词，这样服务器端不需要集成分词组件。大大减少了定制修改的工作量。
- Windows系统cmd窗口默认是GBK编码，即便自己修改成utf-8，仍有不少问题。干脆就用gbk编码发送给win下的服务器端。收到的信息采用utf8解码。
- Linux则比较简单，直接使用utf-8即可。如果是远程服务器，填入外网IP地址即可。
