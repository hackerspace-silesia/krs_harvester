angular.module('Data', ['chart.js'])
.controller("LineCtrl", function ($scope, $routeParams,organizationsData) {





  $scope.labels = ["2000", "2001", "2002", "2003", "2004"];
  $scope.series = ['Kwota(zł)'];
  $scope.data = [
    [65, 59, 80, 81, 56]

  ];

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
      
angular.module('Data')
  .controller('ChartsController', [ 'chart.js',function ( $http) 
{		
}]);

  angular.module('Data')
  .controller('DataCtrl',['organizationsData',function ( organizationsData) 
{	this.sum="557 563 428";
	this.organizationsTestDataArray = {};

	var organizations=this;
  	var init = function () 
	{
		getData();
		console.log(organizations.organizationsTestDataArray);
	};

	var getData = function(){
		organizationsData.getData().then(function(data)	
	    {	let organizationData = {};
	      	for(let i=1;i<11;i++){
	      		let id = data[i].pk;
	   
	      		organizationData[id]={'name':{}};
	      		organizationData[id]['name']=data[i].name;
	      	}
	      
	      		organizations.organizationsTestDataArray = organizationData;
	     
	    });

	}

	init();	


}]);
        