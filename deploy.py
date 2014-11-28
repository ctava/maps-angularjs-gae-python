# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import time
import requests

#Variables
local_hostname = 'http://localhost:8080'
remote_hostname = 'https://<your_gae_app_name_here>.appspot.com'

experiments_endpoint = '/v1/tests'

apiKey = 'your_key_here'

#Functions
def putTests(hostName,endpoint,apiKey,applicationName):
    payload = 'apiKey='+str(apiKey)+'&applicationName='+str(applicationName)
    print payload
    r = requests.put(hostName+endpoint, params=payload)
    print r.text

#Main Script
print "Start"        
beginTime = time.time();  

#change me
hostName = local_hostname

#make this configuration
putTests(hostName,experiments_endpoint,apiKey,"app1")

endTime = time.time();  

print "End"
print endTime - beginTime , " secs to put data into the cloud." 
           
