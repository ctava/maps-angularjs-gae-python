'use strict';

angular.module('myApp.controllers', [])

  .controller('ApplicationsController', ['$scope','$route','Application','Experiment','Variation','Test', function($scope,$route,Application,Experiment,Variation,Test) {
    //Instantiate $scope objects (Best Practices)
    $scope.currentApplication = null;
    $scope.applications = null;

    $scope.currentExperiment = null;
    $scope.experiments = null;

    $scope.currentVariation = null;
    $scope.variations = null;

    $scope.currentTest = null;

    $scope.getApplications = function() {
      console.log('getApplications');
      Application.query({},function(data) {
        console.log(data);
        $scope.applications = data;
      });
    };

    $scope.getExperimentsForApplication = function(applicationID) {
      console.log('getExperimentsForApplication');
      Experiment.query({'applicationID': applicationID},function(data) {
        console.log(data);
        $scope.experiments = data;
      });
    };

    $scope.getVariationsForExperiment = function(experimentID) {
      console.log('getVariationsForExperiment');
      Variation.query({'experimentID': experimentID},function(data) {
        console.log(data);
        $scope.variations = data;
      });
    };

    $scope.showOnlyApplications = function() {
      console.log('showOnlyApplications');
      $scope.currentApplication = null; //forces to show applications table view
      $scope.currentExperiment = null; //forces to show experiments table view
      $scope.currentVariation = null; //forces to show variations table view
    };

    $scope.showAllApplications = function() {
      console.log('showAllApplications');
      $scope.currentApplication = null; //forces to show applications table view
    };

    $scope.showAllExperiments = function() {
      console.log('showAllExperiments');
      $scope.currentExperiment = null; //forces to show experiments table view
    };    

    $scope.showAllVariations = function() {
      console.log('showAllVariations');
      $scope.currentVariation = null; //forces to show variations table view
    };  

    $scope.showApplication = function(applicationID) {
      console.log('showApplication ' + applicationID);
      $scope.currentApplication = _.find($scope.applications,{'applicationID': applicationID});
      console.log($scope.currentApplication); 
    };

    $scope.addApplication = function() {
      console.log('addApplication');
      $scope.currentApplication = new Application();
      $scope.currentApplication.applicationID = guid();
      $scope.currentApplication.experimentAvailable = 0;
      $scope.currentApplication.variationAvailable = 0;
      $scope.currentApplication.experimentPublished = 0;
      console.log($scope.currentApplication);
    };   

    $scope.saveApplication = function() {
      console.log('saveApplication ' + $scope.currentApplication.applicationID + $scope.currentApplication.$$hashKey);
      Application.save($scope.currentApplication,{}, function(data,headers) {
        console.log('save success');
        $scope.getApplications();
        $route.reload()
        $scope.currentApplication = null; //forces to show applications table view
      }, function(response) {
        console.log('save failed'); 
        alert('Save Failed');
        $scope.currentApplication = null; //forces to show applications table view              
      });
    }; 

    $scope.publishExperiments = function(applicationID) {
      console.log('publishExperiments ' + applicationID);
        $scope.currentTest = new Test();
        $scope.currentTest.apiKey = 'your_key_here';
        $scope.currentTest.testID = guid();
        $scope.currentApplication = _.find($scope.applications,{'applicationID': applicationID});
        $scope.currentTest.applicationID = $scope.currentApplication.applicationID;
        $scope.currentTest.applicationName = $scope.currentApplication.applicationName;
        Test.save($scope.currentTest,{}, function(data,headers) {
        console.log('publishExperiments success');
        $scope.currentApplication.experimentPublished = 1;
        $scope.saveApplication();
      }, function(response) {
        console.log('publishExperiments failed'); 
        alert('publish experiments failed');
      });
    }; 

    $scope.unpublishExperiments = function(applicationID) {
      console.log('unpublishExperiments ' + applicationID);;
        $scope.currentApplication = _.find($scope.applications,{'applicationID': applicationID});
        Test.remove($scope.currentApplication,{}, function(data,headers) {
        console.log('unpublishExperiments success');
        $scope.currentApplication.experimentPublished = 0;
        $scope.saveApplication();
      }, function(response) {
        console.log('unpublishExperiments failed'); 
        alert('unpublishing experiments Failed');
      });
    }; 

    $scope.deleteApplication = function(applicationID) {
      console.log('deleteApplication');
      var answer = confirm('Delete Application?');
      if (answer) {
        $scope.currentApplication = _.find($scope.applications,{'applicationID': applicationID});
        Application.remove($scope.currentApplication, function(data,headers) {
          console.log('delete success');
          $scope.getApplications();
          $scope.currentApplication = null; //forces to show applications table view 
          $route.reload();
        }, function(response) {
          console.log('delete failed');
          alert('Delete Failed'); 
          $scope.currentApplication = null; //forces to show applications table view            
        });
      }
    }; 

    $scope.showExperiment = function(experimentID) {
      console.log('showExperiment ' + experimentID);
      $scope.currentExperiment = _.find($scope.experiments,{'experimentID': experimentID});
      console.log($scope.currentExperiment); 
    };

    $scope.addExperiment = function() {
      console.log('addExperiment');
      $scope.currentExperiment = new Experiment();
      $scope.currentExperiment.applicationID = $scope.currentApplication.applicationID;
      $scope.currentExperiment.experimentID = guid();
      console.log($scope.currentExperiment);
    };   

    $scope.saveExperiment = function() {
      console.log('saveExperiment ' + $scope.currentExperiment.experimentID + $scope.currentExperiment.$$hashKey);
      Experiment.save($scope.currentExperiment,{}, function(data,headers) {
        console.log('save success');
        $scope.currentApplication.experimentAvailable = 1;
        $scope.saveApplication();
        $scope.getExperimentsForApplication($scope.currentApplication.applicationID);
        $route.reload()
        $scope.currentExperiment = null; //forces to show experiments table view 
      }, function(response) {
        console.log('save failed'); 
        alert('Save Failed');
        $scope.currentExperiment = null; //forces to show experiments table view              
      });
    }; 

    $scope.deleteExperiment = function(applicationID,experimentID) {
      console.log('deleteExperiment ' + experimentID);
      var answer = confirm('Delete Experiment?');
      if (answer) {
        $scope.currentExperiment = _.find($scope.experiments,{'experimentID': experimentID});
        Experiment.remove($scope.currentExperiment, function(data,headers) {
          console.log('delete success');
          $scope.getExperimentsForApplication($scope.currentApplication.applicationID);
          $scope.currentExperiment = null; //forces to show experiments table view
          $route.reload();
        }, function(response) {
          console.log('delete failed');
          alert('Delete Failed'); 
          $scope.currentExperiment = null; //forces to show experiments table view           
        });
      }
    };   

    $scope.showVariation = function(variationID) {
      console.log('showVariation ' + variationID);
      $scope.currentVariation = _.find($scope.variations,{'variationID': variationID});
      console.log($scope.currentVariation); 
    };

    $scope.addVariation = function(applicationID,experimentID) {
      console.log('addVariation');
      $scope.currentVariation = new Variation();
      $scope.currentVariation.applicationID = applicationID;
      $scope.currentVariation.experimentID = experimentID;
      $scope.currentVariation.variationID = guid();
      console.log($scope.currentVariation);
    };    

    $scope.saveVariation = function() {
      console.log('saveVariation');
      Variation.save($scope.currentVariation,{}, function(data,headers) {
        console.log('success sucess');
        $scope.currentApplication.variationAvailable = 1;
        $scope.saveApplication();
        $scope.getVariationsForExperiment($scope.currentExperiment.experimentID);
        $scope.currentVariation = null; //forces to show variations table view
        $route.reload();
      }, function(response) {
        console.log('save failed'); 
        alert('Save Failed');
        $scope.currentVariation = null; //forces to show variations table view             
      });
    }; 

    $scope.deleteVariation = function(variationID) {
      console.log('deleteVariation');
      var answer = confirm('Delete Variation?');
      if (answer) {
        $scope.currentVariation = _.find($scope.variations,{'variationID': variationID});
        Variation.remove($scope.currentVariation, function(data,headers) {
          console.log('delete success');
          $scope.getVariationsForExperiment($scope.currentExperiment.experimentID);
          $scope.currentVariation = null; //forces to show variations table view
          $route.reload();
        }, function(response) {
          console.log('delete failed');
          alert('Delete Failed'); 
          $scope.currentVariation = null; //forces to show variations table view                
        });
      }
    };     

    $scope.showExperimentsForApplication = function(applicationID) {
      console.log('showExperimentsForApplication ' + applicationID);
      $scope.getExperimentsForApplication(applicationID);
    };

    $scope.showVariationsForExperiment = function(experimentID) {
      console.log('showVariationsForExperiment ' + experimentID);
      $scope.getVariationsForExperiment(experimentID);
    };

    $scope.getApplications();
  }]);