
'use strict';
angular.module('Data')
  .factory('organizationsData', function (Restangular) {
  return {
        getData: function() 
        {          
            
        var baseAccounts = Restangular.all('organizations');

        return baseAccounts.getList();
  
        }
    };
  });