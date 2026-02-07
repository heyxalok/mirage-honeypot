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
def log_credentials(ip,username,password):
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry=f"[{timestamp}] {ip} tried -> user : {username} | pass: {password}\n"
    print(f"[!] Login attempt from {ip} -> {username}/{password}")
    with open("logs/credentials.log","a") as f:
        f.write(entry)
def recv_line(client):
    data=b""
    while True:
        chunk=client.recv(1)
        if not chunk:
            break
        if chunk == b"\r" and not data:
            continue;
        if chunk ==b"\n":
            break
        data+=chunk
    return data.decode(errors="ignore").strip()
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
            client.send(b"Welcome to Secure Server v1.0\n")
            client.send(b"login: ")
            username=recv_line(client)
            client.send(b"password: ")
            password=recv_line(client)
            log_credentials(ip,username,password)
            client.send(b"\nAccess denied\n")
        except Exception as e:
            print("Error:",e)
        client.close()
if __name__=="__main__":
    start_server()