#!/usr/bin/env python

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port, user_message):
  """ A simple echo client """
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Connect the socket to the server
  server_address = (host, port)
  print "Connecting to %s port %s" % server_address
  sock.connect(server_address)
  # Send data
  try:
    # Send data
    message = user_message
    print "Sending %s" % message
    sock.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
      data = sock.recv(16)
      amount_received += len(data)
      print "Received: %s" % data

  except socket.errno, e:
    print "Socket error: %s" %str(e)
  except Exception, e:
    print "Other exception: %s" %str(e)

  finally:
    print "Closing connection to the server"
    sock.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Socket Server Example')
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  parser.add_argument('--user_message', action="store", dest="user_message", type=str, required=False)
  given_args = parser.parse_args()
  port = given_args.port
  user_message = given_args.user_message
  echo_client(port, user_message)
