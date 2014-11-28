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
from appconfig import Experiment, Variation

class ExperimentsHandler(webapp2.RequestHandler):

    def get(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'            
        q = db.Query(Experiment) 
        applicationID=self.request.get('applicationID')
        if applicationID:
            q.filter('applicationID',applicationID)
        if (q.count > 0):
          self.response.out.write(json.dumps([experiment.to_dict() for experiment in q])) 
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
        experimentName = self.request.get("experimentName")   
        if (not experimentName):
            self.response.write('{"error":"true","comments","experimentName is missing"}')
            return 
        experimentRecruitmentDuration = self.request.get("experimentRecruitmentDuration")
        if (not experimentRecruitmentDuration):
            self.response.write('{"error":"true","comments","experimentRecruitmentDuration is missing"}')
            return
        experimentDuration = self.request.get("experimentDuration")
        if (not experimentDuration):
            self.response.write('{"error":"true","comments","experimentDuration is missing"}')
            return
        experimentStartDate = self.request.get("experimentStartDate") 
        if (not experimentStartDate):
            self.response.write('{"error":"true","comments","experimentStartDate is missing"}')
            return                                                
        experiment = Experiment(key_name=str(experimentID),applicationID=str(applicationID),experimentID=str(experimentID),experimentName=str(experimentName),experimentRecruitmentDuration=int(experimentRecruitmentDuration),experimentDuration=int(experimentDuration),experimentStartDate=str(experimentStartDate))
        experiment.put()
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
        experimentName = self.request.get("experimentName")   
        if (not experimentName):
            self.response.write('{"error":"true","comments","experimentName is missing"}')
            return 
        experimentRecruitmentDuration = self.request.get("experimentRecruitmentDuration")
        if (not experimentRecruitmentDuration):
            self.response.write('{"error":"true","comments","experimentRecruitmentDuration is missing"}')
            return
        experimentDuration = self.request.get("experimentDuration")
        if (not experimentDuration):
            self.response.write('{"error":"true","comments","experimentDuration is missing"}')
            return
        experimentStartDate = self.request.get("experimentStartDate") 
        if (not experimentStartDate):
            self.response.write('{"error":"true","comments","experimentStartDate is missing"}')
            return                                                 
        experiment = Experiment(key_name=str(experimentID),applicationID=str(applicationID),experimentID=str(experimentID),experimentName=str(experimentName),experimentRecruitmentDuration=int(experimentRecruitmentDuration),experimentDuration=int(experimentDuration),experimentStartDate=str(experimentStartDate))
        experiment.put()
        self.response.write('{"error":"false"}')         
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])

    def delete(self):
      try:
        self.response.headers['Content-Type'] = 'application/json'      
        applicationID=self.request.get('applicationID')
        experimentID=self.request.get('experimentID')
        varQuery = db.Query(Variation) 
        varQuery.filter('applicationID',applicationID)
        varQuery.filter('experimentID',experimentID)
        expQuery = db.Query(Experiment) 
        expQuery.filter('applicationID',applicationID)
        expQuery.filter('experimentID',experimentID)
        for variation in varQuery:
            variation.delete();
        for experiment in expQuery:
            experiment.delete();
        self.response.write("{\"error\":\"false\"}")
      except:
        self.response.write("{\"error\":\"true\"}")        
        logging.error(sys.exc_info()[0])        
        logging.error(sys.exc_info()[1])
        logging.error(sys.exc_info()[2])
