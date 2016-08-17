#!/usr/bin/env python2.7

import sys, getopt, os.path, os, requests

#verifico se esiste il file EGBL.config
def usage():
	print ""
	print "######## Fortinet NSA checking tool ############"
	print "######## Author by Fabio Natalucci #############"
	print "# with collaboration of NSA and Equation Group #"
	print "#   Thanks to Shadow Brokers for disclosure    #"
	print "################################################"
	print "USAGE: ./check_fortinet_ip -i IP"
	print ""
	print ""

def verifyConfig():
	if os.path.exists("EGBL.config"):
		print '## EGBL.config...OK'
	else: sys.exit(2)

def verifyVuln(n):
	#conn = httplib.HTTPConnection("http://"+n, )
	#conn.request("HEAD", "/")
	#res = conn.getresponse()
	#print res.()*/
	r = requests.get('https://'+n, verify=False)
	etag = r.headers['ETag'].replace('"',"").split('_',2)[-1]
	if etag in open('EGBL.config').read():
		print ''
		print 'Il sistema risulta VULNERABILE'


def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hi:d", ["ip="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	if not opts:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-h":
			print '### HELP? ma LOL ###'
			sys.exit()
		elif opt == "-i":
			ipToCheck = arg
		 

	print '## Checking IP:',arg

	print '## Verify EGBL...'
	verifyConfig()
	 
	print '## Check vulnerability...'
	verifyVuln(ipToCheck)

if __name__ == "__main__":
	main(sys.argv[1:])
