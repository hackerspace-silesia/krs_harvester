angular.module('ChartCity', ['chart.js'])
.controller("ChartCityCtrl", function ($scope, $routeParams, donationsAggData) {
	var vm = this;

  $scope.labels = ["2000", "2001", "2002", "2003", "2004"];
  $scope.series = ['Kwota (zł)'];
  $scope.data = [];

  var init = function(){
  	getGraphs();
  };

  var getGraphs = function(){
		donationsAggData.getSummary('city').then(function(data)	{
			$scope.labels = data.map(function (val) {return val.city});
			$scope.data = data.map(function (val) {return val.sum_money});
		});
	};

  init();

  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
  	title:{
  		display: true,
  		text: 'Dotacja'
  	},
    elements: { line: {tension: 0} },
    scales: {
      yAxes: [
        {
          id: 'y-axis-1',
          type: 'linear',
          display: true,
          position: 'left'
        }
      ]
    }
  };
});
      
