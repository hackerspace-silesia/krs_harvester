angular.module('Charts', ["chart.js"]).controller("LineCtrl", function ($scope) {

  $scope.labels = ["2000", "2001", "2002", "2003", "2004"];
  $scope.series = ['Kwota(zł)'];
  $scope.data = [
    [65, 59, 80, 81, 56]

  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };

    $scope.setSelected = function (a,b,c,d,e) {
    changeData(a,b,c,d,e);
  };

  function changeData(a,b,c,d,e){
		let data = [a,b,c,d,e];
		$scope.data = data;
  }

  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
  	title:{
  		display:true,
  		text:'Dotacja w zależnosci od wybranej dotacji z tabeli'
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
      
angular.module('Charts')
  .controller('ChartsController', [ 'chart.js',function ( $http) 
{		
}]);
        