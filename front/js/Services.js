
'use strict';
angular.module('Data')
  .factory('organizationsData', function (Restangular) {

  return {
        getDataCompareToPartOfName: function(name) 
        {          
            
          let base = Restangular.all('organizations');
          
          return base.getList({search:name});

        },
        getOneOrganizationSpecificData: function(id)
        {
           let organization = Restangular.all('organizations/'+id);

          return organization.getList();
        }
    };
  });