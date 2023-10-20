# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Austin Huang
# austh10@uci.edu
# 28821105

import json
from collections import namedtuple
from Profile import Post


# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['foo', 'baz'])


def extract_json(json_msg: str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object

  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  '''
  try:
    json_obj = json.loads(json_msg)
    foo = json_obj['foo']
    baz = json_obj['bar']['baz']
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return DataTuple(foo, baz)


def send_json(username, password):
  return {"join": {"username": f'{username}', "password": f'{password}', "token": ""}}


def join(username, password):
  return json.dumps({"join": {"username": username, "password": password, "token": ""}})


def response_process(response):
  json_resp = json.loads(response.decode('utf-8').strip())
  return json_resp

def getting_token(json_resp):
  user_token = json_resp['response']['token']
  if json_resp["response"]["type"] != "ok":
    return False
  return user_token


def create_biomessage(user_token, bio):
  return json.dumps({"token": user_token, "bio": {"entry": bio}})


def handling_response(response):
  json_resp = json.loads(response.decode('utf-8').strip())
  if json_resp["response"]["type"] != "ok":
    return False
  user_token = json_resp['response']['token']
  return user_token


def post_bio(message, bio, user_token):
  if message and bio is None:
    return json.dumps({"token": user_token, "post": {"entry": message}})
  elif message and bio:
    return json.dumps({"token": user_token, "bio": {"entry": bio}})


def creating_postmessage(user_token, message):
  post_message = json.dumps({"token": user_token, "post": {"entry": f'{message}', "timestamp": f'{Post(message).get_time()}'}})
  return (post_message)


def parsing_response(response):
  json_resp = json.loads(response.decode('utf-8').strip())
  if json_resp["response"]["type"] != "ok":
    return False
  return True
