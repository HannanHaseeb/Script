#!/usr/bin/python

from sys import argv
import time
import os
import urllib2
import requests

print'''
       \033[3;37;37m Subdomain Status Code Checker \033[3;31;31m
'''
print'''
            \033[3;37;37m By Hannan Haseeb \033[3;31;31m
'''
       

script, filename = argv
f= open(filename,"r+");
subdomains = f.readlines();
count = 0;

for subdomain in subdomains:
    newsubdomain="http://%s" % subdomain
    try:
      a=urllib2.urlopen(newsubdomain)
      code=a.getcode();
      print "Domain :  %sCode: %d" % (newsubdomain,code)
    except urllib2.HTTPError, e:
           code = e.code
           print "Domain : %sCode: %d" % (newsubdomain,code)
    except urllib2.URLError, e:
           print "Domain: %s DNS address could not be found" % newsubdomain

