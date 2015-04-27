#!/usr/bin/env python
import argparse

from ngflaskcurd import create_app

parser = argparse.ArgumentParser(description="Run ngflaskcurd App")
parser.add_argument('-p', '--port', help='App Port')
parser.add_argument('--host', help='App Host')
parser.add_argument('-r', action='store_true', help='Turn reloader on')
args = parser.parse_args()

host = args.host or '0.0.0.0'
port = int(args.port) if args.port else 5000
reloader = args.r or False

app = create_app()
app.run(use_reloader=reloader, host=host, port=port)
