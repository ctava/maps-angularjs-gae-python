# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2014 Christopher Tava
#
import webapp2
from google.appengine.ext import db
from google.appengine.api import memcache
import logging
import sys
import json
from appconfig import Test, Application, Experiment, Variation

apiKeys = ['your_key_here']

class TestsHandler(webapp2.RequestHandler):

    def get(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'  
        apiKey = self.request.get("apiKey")   
        if (not apiKey):
            self.response.write('{"error":"true","comments","apiKey is missing"}')
            return
        if apiKey not in apiKeys :
            self.response.write('{"error":"true","comments","apiKey invalid"}')
            return 
        applicationName=self.request.get('applicationName')
        if applicationName:
            response = memcache.get(applicationName)
            if response:
                self.response.out.write(response)
                return
        else:
            self.response.write("{\"error\":\"false\"}")
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])

    def post(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'
        apiKey = self.request.get("apiKey")   
        if (not apiKey):
            self.response.write('{"error":"true","comments","apiKey is missing"}')
            return
        if apiKey not in apiKeys :
            self.response.write('{"error":"true","comments","apiKey invalid"}')
            return
        applicationName = self.request.get("applicationName")   
        if (not applicationName):
            self.response.write('{"error":"true","comments","applicationName is missing"}')
            return
        appQuery = db.Query(Application) 
        appQuery.filter('applicationName',applicationName)
        response = ''
        for application in appQuery: 
            logging.info('found application '+ str(application.applicationID))
            expQuery = db.Query(Experiment)
            expQuery.filter('applicationID',application.applicationID)
            expIteration = 0;
            for experiment in expQuery:
                expIteration += 1
                logging.info('found experiment '+ str(experiment.experimentID))
                if expIteration == 1:
                    response = '['
                if expIteration >= 1:
                    response += '{"experimentID":"'+experiment.experimentID+'","experimentName":"'+experiment.experimentName+'","experimentRecruitmentDuration":'+str(experiment.experimentRecruitmentDuration)+',"experimentDuration":'+str(experiment.experimentDuration)+',"experimentStartDate":"'+str(experiment.experimentStartDate)+'"'
                varQuery = db.Query(Variation)
                varQuery.filter('applicationID',application.applicationID)
                varQuery.filter('experimentID',experiment.experimentID)
                varIteration = 0;
                for variation in varQuery:
                    varIteration += 1
                    logging.info('found variation '+ str(variation.variationID))
                    if varIteration == 1:
                        response += ',"variations":['
                    if varIteration >= 1:
                        response += '{"variationID":"'+variation.variationID+'","variationName":"'+variation.variationName+'","variationPercentage":'+str(variation.variationPercentage)
                    if varIteration != varQuery.count():
                        response += '},'
                    if varIteration == varQuery.count():
                        response += '}]'
                if expIteration != expQuery.count():
                    response += '},'
                if expIteration == expQuery.count():
                    response += '}]'
        memcache.add(key=applicationName, value=str(response))
        self.response.write('{"error":"false"}')         
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])

    def post(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'
        apiKey = self.request.get("apiKey")   
        if (not apiKey):
            self.response.write('{"error":"true","comments","apiKey is missing"}')
            return
        if apiKey not in apiKeys :
            self.response.write('{"error":"true","comments","apiKey invalid"}')
            return
        applicationName = self.request.get("applicationName")   
        if (not applicationName):
            self.response.write('{"error":"true","comments","applicationName is missing"}')
            return
        appQuery = db.Query(Application) 
        appQuery.filter('applicationName',applicationName)
        response = ''
        for application in appQuery: 
            logging.info('found application '+ str(application.applicationID))
            expQuery = db.Query(Experiment)
            expQuery.filter('applicationID',application.applicationID)
            expIteration = 0;
            for experiment in expQuery:
                expIteration += 1
                logging.info('found experiment '+ str(experiment.experimentID))
                if expIteration == 1:
                    response = '['
                if expIteration >= 1:
                    response += '{"experimentID":"'+experiment.experimentID+'","experimentName":"'+experiment.experimentName+'","experimentRecruitmentDuration":'+str(experiment.experimentRecruitmentDuration)+',"experimentDuration":'+str(experiment.experimentDuration)+',"experimentStartDate":"'+str(experiment.experimentStartDate)+'"'
                varQuery = db.Query(Variation)
                varQuery.filter('applicationID',application.applicationID)
                varQuery.filter('experimentID',experiment.experimentID)
                varIteration = 0;
                for variation in varQuery:
                    varIteration += 1
                    logging.info('found variation '+ str(variation.variationID))
                    if varIteration == 1:
                        response += ',"variations":['
                    if varIteration >= 1:
                        response += '{"variationID":"'+variation.variationID+'","variationName":"'+variation.variationName+'","variationPercentage":'+str(variation.variationPercentage)
                    if varIteration != varQuery.count():
                        response += '},'
                    if varIteration == varQuery.count():
                        response += '}]'
                if expIteration != expQuery.count():
                    response += '},'
                if expIteration == expQuery.count():
                    response += '}]'
        memcache.add(key=applicationName, value=str(response))
        self.response.write('{"error":"false"}')         
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])
        
    def delete(self):
      try:
        self.response.headers['Content-Type'] = 'application/json' 
        apiKey = self.request.get("apiKey")   
        if (not apiKey):
            self.response.write('{"error":"true","comments","apiKey is missing"}')
            return
        if apiKey not in apiKeys :
            self.response.write('{"error":"true","comments","apiKey invalid"}')
            return
        applicationName=self.request.get('applicationName')  
        if (not applicationName):
            self.response.write('{"error":"true","comments","applicationName is missing"}')
            return
        memcache.delete(key=applicationName)    
        self.response.write("{\"error\":\"false\"}")
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])
