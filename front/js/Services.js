
'use strict';
angular.module('Data')
  .factory('organizationsData', function (Restangular) {
  return {
        getDataCompareToPartOfName: function(name) 
        {          
            
          var base = Restangular.all('organizations');
          
          return base.getList({search:name});

        },
        getOneOrganization: function(id)
        {
           var organization = Restangular.all('organizations/'+id);

          return organization.getList();
        }
    };
  });