angular.module('Data', ['chart.js'])
.controller("LineCtrl", function ($scope, $routeParams,organizationsData) {
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

  angular.module('Data')
  .controller('DataCtrl',['organizationsData','$location','$window',function ( organizationsData, $location,$window) 
{	
	var organizations=this;

	organizations.sum="557 563 428";
	organizations.organizationsTestDataArray = {};
	organizations.writings;


	organizations.showOrganizationData=function(){

		let id = getId(organizations.writings);

		$location.path('#/organisation/'+id+'/');
		$window.location.assign('#/organisation/'+id+'/');
	}

	getId = function(name){
		let organizationTest = organizations.organizationsTestDataArray;

		for(let i =1;i<10;i++){
			if(organizationTest[i].name=name)
			{
				return organizationTest[i].id;
			}
			return 0;
		}

	}

	organizations.getName = function(id){
		let organizationTest = organizations.organizationsTestDataArray;

		for(let i =1;i<10;i++){
			if(organizationTest[i].name=name)
			{
				return organizationTest[i].name;
			}
			return '';
		}

	}

	organizations.getData = function(partOfName){
		organizationsData.getDataCompareToPartOfName(partOfName).then(function(data)	
	    {	    		console.log(partOfName);
	    		getNamePropositionsOrganization(data);    		
	    });
	}

	var getNamePropositionsOrganization = function (arrayOfObjectOrganisations)
	{	
		let data = arrayOfObjectOrganisations;
		let organizationData = {};
	
	      	for(let i=0;i<10;i++){
	      		if(typeof data[i] =='object')
	      		{
		      		let id = data[i].pk;
		      		organizationData[i]={'name':{}};
		      		organizationData[i]['name']=data[i].name;
		      		organizationData[i]['id']=id;
	      		}
	      	}
	      
	      	organizations.organizationsTestDataArray=organizationData;
	      console.log(organizationData);
		}




}]);
        