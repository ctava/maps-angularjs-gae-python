'use strict';

// Declare app level module which depends on filters, and services
angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives', 'myApp.controllers', 'myApp.animations','ngRoute','ngAnimate']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/applications', {templateUrl: '../app/applications.html', controller: 'ApplicationsController'});
    $routeProvider.otherwise({redirectTo: '/applications'});
  }]);
