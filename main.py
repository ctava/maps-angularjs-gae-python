# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2014 Christopher Tava
#
import webapp2

from appconfig import User
from home import HomeHandler, ApplicationHandler, SignupHandler, VerificationHandler, SetPasswordHandler, LoginHandler, LogoutHandler, ForgotPasswordHandler
from confirm import ConfirmUserSignup
from applications import ApplicationsHandler
from experiments import ExperimentsHandler
from variations import VariationsHandler
from tests import TestsHandler

config = {
  'webapp2_extras.auth': {
    'user_model': 'appconfig.User',
    'user_attributes': ['name']
  },
  'webapp2_extras.sessions': {
    'secret_key': 'YOUR_SECRET_KEY'
  }
}

app = webapp2.WSGIApplication([
    webapp2.Route('/', HomeHandler, name='home'),
    webapp2.Route('/signup', SignupHandler),
    webapp2.Route('/<type:v|p>/<user_id:\d+>-<signup_token:.+>',
      handler=VerificationHandler, name='verification'),
    webapp2.Route('/password', SetPasswordHandler),
    webapp2.Route('/login', LoginHandler, name='login'),
    webapp2.Route('/logout', LogoutHandler, name='logout'),
    webapp2.Route('/forgot', ForgotPasswordHandler, name='forgot'),
    webapp2.Route('/application', ApplicationHandler, name='application'),
	  ('/v1/applications',ApplicationsHandler),
    ('/v1/experiments',ExperimentsHandler),
    ('/v1/variations',VariationsHandler),
    ('/v1/tests',TestsHandler),
], config=config, debug=True)

def main():
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
    main()
