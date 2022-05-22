import socket
import time

class app():

    print("[+] ====== hx7 Script ====== [+]")
    time.sleep(0.7)
    print("[+] ====== Port Grabber By: [Port Name] ====== [+]")
    time.sleep(0.7)
    print("[+] ====== Made By: hx7 | hadixd ====== [+]")
    time.sleep(1)
    print("> 1")
    time.sleep(2)
    print("> 2")
    time.sleep(1)
    print("> 3")
    time.sleep(0.7)
    print("> ------ | 10%")
    time.sleep(0.7)
    print("> ----------- | 50%")
    time.sleep(1)
    print("> ---------------- | 100%")
    time.sleep(1)

    print("> Welcome 👋")
    time.sleep(0.7)
    print(' ')
    portname = input("> Enter Port Name : ")
    ftls = socket.getservbyname(portname)
    print(ftls)

app()