import socket
import select

HEAD_LEN = 10

IP = "127.0.0.1"
PORT = 3000


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ss.bind((IP, PORT))

ss.listen()


sockets_arr = [ss]

clients = {}

print(f'Listening for connections on {IP}:{PORT}...')

def receive_message(client_socket):

    try:

        message_header = client_socket.recv(HEAD_LEN)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
  
        return False

while True:

 
    read_sockets, _, exception_sockets = select.select(sockets_arr, [], sockets_arr)


    for notified_socket in read_sockets:
        if notified_socket == ss:

          
            client_socket, client_address = ss.accept()

            user = receive_message(client_socket)

            if user is False:
                continue

            sockets_arr.append(client_socket)

            clients[client_socket] = user


        else:

            message = receive_message(notified_socket)

            if message is False:

                sockets_arr.remove(notified_socket)

                del clients[notified_socket]

                continue

            user = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:

                if client_socket != notified_socket:

                   
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:

        sockets_arr.remove(notified_socket)

        del clients[notified_socket]

