import socket
from datetime import datetime
HOST="0.0.0.0"
PORT=2222
def log_connection(ip,port):
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry=f"[{timestamp}] Connection from {ip}:{port}\n"
    print(f"[+] Connection detected->{ip}:{port}")
    with open("logs/connections.log","a") as f:
        f.write(entry)
def start_server():
    print(f"[Mirage] Listening on port {PORT}...")
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen(5);
    while True:
        client,addr=server.accept()
        ip,port=addr
        log_connection(ip,port)
        try:
            client.send(b"Welcome to Secure Server\n")
        except:
            pass
        client.close()
if __name__=="__main__":
    start_server()