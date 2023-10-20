# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Austin Huang
# austh10@uci.edu
# 28821105
import socket
import json
import ds_protocol
from Profile import Post


def send(server: str, port: int, username: str, password: str, message: str, bio: str = None):
    '''
    The send function joins a ds server and sends a message, bio, or both

    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((server, port))
      try:
          with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
              srv.connect((server, port))
              joining_message = ds_protocol.join(username, password)
              srv.sendall((joining_message + "\n").encode('utf-8'))
              response = srv.recv(4096)
              json_resp = ds_protocol.response_process(response)
              print(f'The response:', json_resp)
              json_resp1= ds_protocol.getting_token(json_resp)
              if bio is not None and bio != '' and bio != ' ':
                  bio_message = ds_protocol.create_biomessage(json_resp1, bio)
                  srv.sendall((bio_message + "\n").encode('utf-8'))
                  response = srv.recv(4096)
                  json_resp = ds_protocol.post_bio(message, bio, json_resp1)
                  srv.sendall((json_resp + "\n").encode('utf-8'))
              elif message is not None and message != '' and message != ' ':
                  post_message = ds_protocol.creating_postmessage(json_resp1, message)
                  srv.sendall((post_message + "\n").encode('utf-8'))
                  response = srv.recv(4096)
                  json_resp = ds_protocol.post_bio(message, bio, json_resp1)
                  srv.sendall((json_resp + "\n").encode('utf-8'))
              else:
                  return False
              return True
      except (socket.gaierror, ConnectionRefusedError, TimeoutError, ConnectionResetError, OSError) as problem:
          print(f'Error when trying to connect to ther server: {problem}')
          return False
