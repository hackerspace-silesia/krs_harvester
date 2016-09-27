
'use strict';
angular.module('Data')
  .factory('organizationsData', function (Restangular) {

  return {
        getDataCompareToPartOfName: function(name) 
        {          
            
          let base = Restangular.all('organizations');
          
          return base.getList({search:name});

        },
        getOne: function(id)
        {
           let organization = Restangular.one('organizations/'+id);
          return organization.get();
        }
    };
  });