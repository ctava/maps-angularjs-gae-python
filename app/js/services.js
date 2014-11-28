'use strict';

angular.module('myApp.services', ['ngResource'])
  .factory('Application', function($resource){
    return $resource('/v1/applications')
  })
  .factory('Experiment', function($resource){
    return $resource('/v1/experiments')
  })
  .factory('Variation', function($resource){
    return $resource('/v1/variations')
  })
  .factory('Test', function($resource){
    return $resource('/v1/tests')
  })
  .value('version', '0.1');