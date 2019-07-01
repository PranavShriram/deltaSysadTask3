import socket
import select
import errno

HEAD_LEN = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")


cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cs.connect((IP, PORT))

cs.setblocking(False)


username = my_username.encode('utf-8')
user_head = f"{len(username):<{HEAD_LEN}}".encode('utf-8')
cs.send(user_head + username)

while True:
    message = input(f'{my_username} > ')

    if message:

        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEAD_LEN}}".encode('utf-8')
        cs.send(message_header + message)

    try:
        while True:

            user_head = cs.recv(HEAD_LEN)

            if not len(user_head):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(user_head.decode('utf-8').strip())

            # Receive and decode username
            username = cs.recv(username_length).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            message_header = cs.recv(HEAD_LEN)
            message_length = int(message_header.decode('utf-8').strip())
            message = cs.recv(message_length).decode('utf-8')

            print(f'{username} > {message}')

    except IOError as e:
   
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        continue
    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()
