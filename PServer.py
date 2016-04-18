#incorporating cli with socket programming

__author__ = "a9393j"
import argparse
import sys
from argparse import RawTextHelpFormatter
from proxy_server import TheServer

def parse_args():
	parser = argparse.ArgumentParser(description="read arbitary data from one socket"
		"and write it to another",formatter_class=RawTextHelpFormatter)
	parser.add_argument("-p",action="store",dest="port",required=True,
						type=int,help="port used to setup the proxy server")
	parser.add_argument("-fh",action="store",dest="fHost",required=True,
						help="Host address of the original server to which the traffic will be forwarded to.")
	parser.add_argument("-fp",action="store",dest="fPort",required=True,
						type=int,help="Port of the original server to which the traffic will be forwarded to.")
	return parser.parse_args()

def main():
	opts = parse_args()
	proxy = TheServer('',
					port=opts.port,
					fHost=opts.fHost,
					fPort=opts.fPort)
	try:
		proxy.main_loop()

	except KeyboardInterrupt:
		print "\nCtrl C - Stopping server"
		sys.exit(1)
	
if __name__== "__main__":
	main()