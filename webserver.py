'''
Simple webserver for local testing
'''
from argparse import ArgumentParser

import SimpleHTTPServer
import SocketServer

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args() 
    
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", args.port), Handler)

    print "Serving at port ", args.port
    httpd.serve_forever()