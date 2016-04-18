# proxysock
(reading arbitary data from one socket and writing it to another)

This repository can be used for creating a proxy server. The proxy server acts as a bridge between the client and original server.

##Usage
```
python PServer.py -h
```
We required three arguments.
-Proxy server port.
-Original server host.
-Original server port.

By providing these three values, we are ready to go.

example-> we can setup a TCP server at localhost:9090 using sockProg repository.

Now use the following command to setup a proxy server at localhost:9191.

```
python PServer.py -p 9191 -fh localhost -fp 9090
```
Now the proxy server is acting as a bridge between the TCP server and the client. 
use Telnet to connect to the proxy server.
```
telnet localhost 9191
```
Now the client can send messages to the TCP server localhost:9090 Via Proxy server at localhost:9191.

