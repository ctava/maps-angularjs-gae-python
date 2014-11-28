maps
====
multivariate
analytics
and performance testing
suite

this is an angularjs rest google app engine (GAE) python application to create applications, experiments with variations.

pre-requisites
be sure to have the GAE python SDK installed: 
https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python

create an application in google app engine dashboard

setup instructions
git clone this repo: https://github.com/ctava/maps-angularjs-gae-python
in google app engine launcher, choose file new, add existing application running on port 8080
be sure that application: entry in app.yaml matches name of application created in google app engine dashboard

now, in google app engine launcher, you can run the application on localhost or deploy to app engine.

to see the user interface, navigate to localhost:8080/app or <app_name>.appspot.com/app/

cli deployment can be done by executing the following from the command line:

appcfg.py update .

python deploy.py

Screenshots

![Alt text](https://github.com/ctava/maps-angularjs-gae-python/blob/master/applications.png "Applications")
![Alt text](https://github.com/ctava/maps-angularjs-gae-python/blob/master/experiments.png "Experiments")
![Alt text](https://github.com/ctava/maps-angularjs-gae-python/blob/master/variations.png "Variations")
![Alt text](https://github.com/ctava/maps-angularjs-gae-python/blob/master/variation.png "Variation")

Experiments, variations are published on an application-by-application basis to memcache
![Alt text](https://github.com/ctava/maps-angularjs-gae-python/blob/master/memcache.png "Memcache")