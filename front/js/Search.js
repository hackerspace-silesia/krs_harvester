  angular.module('Data')
  .controller('SearchCtr',['organizationsData','$location','$window',function ( organizationsData, $location,$window) 
{	
	var search=this;

	search.sum="557 563 428";
	search.organizationsTestDataArray = {};
	search.writings;


	search.showOrganizationData=function(){

		let id = getId(organizations.writings);

		$location.path('#/organisation/'+id+'/');
		$window.location.assign('#/organisation/'+id+'/');
	}

	getId = function(name){
		let organizationTest = search.organizationsTestDataArray;
			
		for(let i =0;i<10;i++){
			console.log(organizationTest[i]);
			if(organizationTest[i].name==name)
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