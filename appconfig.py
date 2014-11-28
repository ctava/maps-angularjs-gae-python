# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2014 Christopher Tava
#
from google.appengine.ext import db

import time
import webapp2_extras.appengine.auth.models

from google.appengine.ext import ndb

from webapp2_extras import security

class User(webapp2_extras.appengine.auth.models.User):
  def set_password(self, raw_password):
    """Sets the password for the current user
    :param raw_password:
        The raw password which will be hashed and stored
    """
    self.password = security.generate_password_hash(raw_password, length=12)

  @classmethod
  def get_by_auth_token(cls, user_id, token, subject='auth'):
    """Returns a user object based on a user ID and token.
    :param user_id:
        The user_id of the requesting user.
    :param token:
        The token string to be verified.
    :returns:
        A tuple ``(User, timestamp)``, with a user object and
        the token timestamp, or ``(None, None)`` if both were not found.
    """
    token_key = cls.token_model.get_key(user_id, subject, token)
    user_key = ndb.Key(cls, user_id)
    # Use get_multi() to save a RPC call.
    valid_token, user = ndb.get_multi([token_key, user_key])
    if valid_token and user:
        timestamp = int(time.mktime(valid_token.created.timetuple()))
        return user, timestamp

    return None, None

class Test(db.Model):
  apiKey = db.StringProperty()
  applicationID = db.StringProperty()
  applicationName = db.StringProperty()
  def to_dict(self):
    return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
    
class Application(db.Model):
  applicationID = db.StringProperty(indexed=True)
  applicationName = db.StringProperty(required=True)
  experimentAvailable = db.IntegerProperty(required=True)
  variationAvailable = db.IntegerProperty(required=True)
  experimentPublished = db.IntegerProperty(required=True)
  def to_dict(self):
    return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

class Experiment(db.Model):
  applicationID = db.StringProperty(indexed=True)
  experimentID = db.StringProperty(indexed=True)
  experimentName = db.StringProperty(required=True)
  experimentRecruitmentDuration   = db.IntegerProperty()
  experimentDuration = db.IntegerProperty()
  experimentStartDate = db.StringProperty()
  def to_dict(self):
    return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

class Variation(db.Model):
  applicationID = db.StringProperty(indexed=True)
  experimentID = db.StringProperty(indexed=True)
  variationID = db.StringProperty(indexed=True)
  variationName = db.StringProperty(required=True)
  variationPercentage = db.IntegerProperty(required=True)
  def to_dict(self):
    return dict([(p, unicode(getattr(self, p))) for p in self.properties()])