angular.module('Data', ['chart.js'])
.controller("LineCtrlOrganization", function ($scope, $routeParams,organizationsData) {

var line = this;
$scope.actualId = $routeParams.name;

$scope.actualName;
		
line.organizationNameId={};

  $scope.labels = ["2000", "2001", "2002", "2003", "2004"];
  $scope.series = ['Kwota(zł)'];
  $scope.data = [
    [65, 59, 80, 81, 56]

  ];

    $scope.setSelected = function (a,b,c,d,e) {
    changeData(a,b,c,d,e);
  };
  

  var getDataOrganisations = function(){
		organizationsData.getDataCompareToPartOfName().then(function(data)	
	    {	let organizationData = {};
	      	for(let i=1;i<11;i++){
	      		let id = data[i].pk;
	      		organizationData[i]={'name':{}};
	      		organizationData[i]['name']=data[i].name;
	      		organizationData[i]['id']=id;
	      	}
	     	line.organizationNameId = organizationData;	
	     	$scope.actualName=getName();
	    });

	};
	getDataOrganisations();
	var getName = function(){
		let organizationTest = line.organizationNameId;

		for(let i =1;i<10;i++){


			if(organizationTest[i].id=$scope.actualId)
			{	console.log(organizationTest[i].name);
				return organizationTest[i].name;
			}
			return '';
		}

	}


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


        