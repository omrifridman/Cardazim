import argparse
import sys
import socket
import struct


def run_server(ip, port):
    '''
    Listens to data at (ip, port)
    '''

    server = socket.socket()
    server.bind((ip, port))
    server.listen(2)

    while True:
        connection, address = server.accept()
        data = connection.recv(1024)

        if data:
            payload_size = struct.unpack("<L", data[:4])[0]
            payload = struct.unpack(f"{payload_size}s", data[4:])[0].decode('utf-8')
            print(f"Received data: {payload}")

        connection.close()


def get_args():
    parser = argparse.ArgumentParser(description='Run server.')
    parser.add_argument('ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('port', type=int,
                        help='the server\'s port')
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and running server.
    '''
    args = get_args()
    try:
        run_server(args.ip, args.port)
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
