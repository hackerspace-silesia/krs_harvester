angular.module('MapWojewodztwa', ['datamaps'])
.controller("MapWojewodztwaCtrl", function ($scope, $routeParams, donationsAggData) {
	var vm = this;

  $scope.labels = ["2000", "2001", "2002", "2003", "2004"];
  $scope.series = ['Kwota (zł)'];
  $scope.data = [];

  var init = function(){
  	getGraphs();
  };

  var getGraphs = function(){
		donationsAggData.getSummary('wojewodztwa').then(function(data)	{
			$scope.labels = data.map(function (val) {return val.wojewodztwa});
			$scope.data = data.map(function (val) {return val.sum_money});
		});
	};

  init();
  $scope.mapObject = {
  scope: 'pol',
  geographyConfig: {
    highlighBorderColor: '#EAA9A8',
    highlighBorderWidth: 2
  },
  fills: {
    'HIGH': '#CC4731',
    'MEDIUM': '#306596',
    'LOW': '#667FAF',
    'defaultFill': '#DDDDDD'
  },
}  
});
      
