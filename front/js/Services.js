
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
  })
  .factory('donationsAggData', function (Restangular) {
    return {
        getSummary: function(group, ordering, limit) {
            var api = Restangular.all('donations-agg');
            return api.getList({
                group: group,
                ordering: ordering || '-sum_money',
                limit: limit || 20
            });
        }
    };
  })
  .factory('Wojewodztwa', function() {
     return {
        "2": "kujawsko-pomorskie",
        "12": "slaskie",
        "9": "podkarpackie",
        "3": "lubelskie",
        "8": "opolskie",
        "14": "warminsko-mazurskie",
        "5": "lodzkie",
        "4": "lubuskie",
        "10": "podlaskie",
        "6": "malopolskie",
        "13": "swietokrzyskie",
        "7": "mazowieckie",
        "15": "wielkopolskie",
        "16": "zachodniopomorskie",
        "11": "pomorskie",
        "1": "dolnoslaskie"
      };
  })
;