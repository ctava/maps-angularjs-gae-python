# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2014 Christopher Tava
#
import webapp2
from google.appengine.ext import db
import logging
import sys
import json
from appconfig import Application, Experiment, Variation

class ApplicationsHandler(webapp2.RequestHandler):

    def get(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'            
        q = db.Query(Application) 
        applicationID=self.request.get('applicationID')
        if applicationID:
            q.filter('applicationID',applicationID)
        if (q.count > 0):
          self.response.out.write(json.dumps([application.to_dict() for application in q])) 
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
        applicationID = self.request.get("applicationID")   
        if (not applicationID):
            self.response.write('{"error":"true","comments","applicationID is missing"}')
            return   
        applicationName = self.request.get("applicationName")   
        if (not applicationName):
            self.response.write('{"error":"true","comments","applicationName is missing"}')
            return 
        experimentAvailable = self.request.get("experimentAvailable")   
        if (not experimentAvailable):
            self.response.write('{"error":"true","comments","experimentAvailable is missing"}')
            return
        variationAvailable = self.request.get("variationAvailable")   
        if (not variationAvailable):
            self.response.write('{"error":"true","comments","variationAvailable is missing"}')
            return 
        experimentPublished = self.request.get("experimentPublished")   
        if (not experimentPublished):
            self.response.write('{"error":"true","comments","experimentPublished is missing"}')
            return                                                  
        application = Application(key_name=str(applicationID),applicationID=str(applicationID),applicationName=str(applicationName),experimentAvailable=int(experimentAvailable),variationAvailable=int(variationAvailable),experimentPublished=int(experimentPublished))
        application.put()
        self.response.write('{"error":"false"}')         
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])

    def put(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'     
        applicationID = self.request.get("applicationID")   
        if (not applicationID):
            self.response.write('{"error":"true","comments","applicationID is missing"}')
            return   
        applicationName = self.request.get("applicationName")   
        if (not applicationName):
            self.response.write('{"error":"true","comments","applicationName is missing"}')
            return 
        experimentAvailable = self.request.get("experimentAvailable")   
        if (not experimentAvailable):
            self.response.write('{"error":"true","comments","experimentAvailable is missing"}')
            return
        variationAvailable = self.request.get("variationAvailable")   
        if (not variationAvailable):
            self.response.write('{"error":"true","comments","variationAvailable is missing"}')
            return 
        experimentPublished = self.request.get("experimentPublished")   
        if (not experimentPublished):
            self.response.write('{"error":"true","comments","experimentPublished is missing"}')
            return                                                  
        application = Application(key_name=str(applicationID),applicationID=str(applicationID),applicationName=str(applicationName),experimentAvailable=int(experimentAvailable),variationAvailable=int(variationAvailable),experimentPublished=int(experimentPublished))
        application.put()
        self.response.write('{"error":"false"}')         
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])

    def delete(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'     
        appQuery = db.Query(Application)  
        applicationID=self.request.get('applicationID')
        appQuery.filter('applicationID',applicationID);
        expQuery = db.Query(Experiment) 
        expQuery.filter('applicationID',applicationID)
        varQuery = db.Query(Variation) 
        varQuery.filter('applicationID',applicationID)
        for variation in varQuery:
            variation.delete();
        for experiment in expQuery:
            experiment.delete();
        for application in appQuery:
            application.delete();
        self.response.write("{\"error\":\"false\"}")
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])
