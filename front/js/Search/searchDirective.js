'use strict';
angular.module('Data')
.directive('searchForOrganization', function() {
  return {
    restrict: 'E',
    templateUrl: 'views/search.html'
  };
});