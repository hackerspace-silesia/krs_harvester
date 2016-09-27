'use strict';
angular.module('Data')
.directive('searchForOrganization', function() {
  return {
  	scope: false,
    restrict: 'E',
    templateUrl: 'views/search.html'
  };
});