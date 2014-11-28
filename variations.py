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
from appconfig import Variation

class VariationsHandler(webapp2.RequestHandler):

    def get(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'            
        q = db.Query(Variation) 
        experimentID=self.request.get('experimentID')
        if experimentID:
            q.filter('experimentID',experimentID)
        if (q.count > 0):
          self.response.out.write(json.dumps([variation.to_dict() for variation in q])) 
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
        experimentID = self.request.get("experimentID")   
        if (not experimentID):
            self.response.write('{"error":"true","comments","experimentID is missing"}')
            return 
        variationID = self.request.get("variationID")   
        if (not variationID):
            self.response.write('{"error":"true","comments","variationID is missing"}')
            return    
        variationName = self.request.get("variationName")   
        if (not variationName):
            self.response.write('{"error":"true","comments","variationName is missing"}')
            return
        variationPercentage = self.request.get("variationPercentage")   
        if (not variationPercentage):
            self.response.write('{"error":"true","comments","variationPercentage is missing"}')
            return                                               
        variation = Variation(key_name=str(variationID),applicationID=str(applicationID),experimentID=str(experimentID),variationID=str(variationID),variationName=str(variationName),variationPercentage=int(variationPercentage))
        variation.put()
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
        experimentID = self.request.get("experimentID")   
        if (not experimentID):
            self.response.write('{"error":"true","comments","experimentID is missing"}')
            return 
        variationID = self.request.get("variationID")   
        if (not variationID):
            self.response.write('{"error":"true","comments","variationID is missing"}')
            return    
        variationName = self.request.get("variationName")   
        if (not variationName):
            self.response.write('{"error":"true","comments","variationName is missing"}')
            return
        variationPercentage = self.request.get("variationPercentage")   
        if (not variationPercentage):
            self.response.write('{"error":"true","comments","variationPercentage is missing"}')
            return                                               
        variation = Variation(key_name=str(variationID),applicationID=str(applicationID),experimentID=str(experimentID),variationID=str(variationID),variationName=str(variationName),variationPercentage=int(variationPercentage))
        variation.put()
        self.response.write('{"error":"false"}')         
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])

    def delete(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'     
        q = db.Query(Variation)          
        variationID=self.request.get('variationID')
        q.filter('variationID',variationID);
        for variation in q:
            variation.delete();
        self.response.write("{\"error\":\"false\"}")
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])        
