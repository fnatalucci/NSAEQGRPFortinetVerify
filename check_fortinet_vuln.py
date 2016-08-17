#!/usr/bin/env python

import sys, getopt, os.path, os, urllib3
import requests 
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#verifico se esiste il file EGBL.config
def usage():
    print ""
    print "######## Fortinet NSA checking tool ############"
    print "# Author:   Fabio Natalucci                    #"
    print "# Twitter: @fabionatalucci                     #"
    print "# Website: https://www.fabionatalucci.it       #"
    print "#                BIG THANKS TO...              #"
    print "#            NSA and Equation Group            #"
    print "#       and to Shadow Brokers for disclosure   #"
    print "################################################"
    print "USAGE: ./check_fortinet_ip -i IP"
    print ""
    print ""

def verifyConfig():
    if os.path.exists("EGBL.config"):
        print '## EGBL.config...OK'
    else: sys.exit(2)

def verifyVuln(n):
    try:
        r=requests.get('https://'+n, verify=False, timeout=10)
    except requests.exceptions.RequestException as e:   
        print e
        sys.exit(1)
    
    #debug print r.headers['ETag']
    etag = r.headers['ETag'].replace('"',"").split('_',2)[-1]
    
    if etag in open('EGBL.config').read():
        print ''
        print '----> VULNERABLE ! '
    else :
        print ''
        print '----> NOT VULNERABLE'


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
