  angular.module('Data')
  .controller('SearchCtr',['organizationsData','$location','$window',function ( organizationsData, $location,$window) 
{	
	var search=this;

	search.sum="557 563 428";
	search.organizationsTestDataArray = {};
	search.writings;


	search.showOrganizationData=function(){

		let id = getId(search.writings);

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

	search.getName = function(id){
		let organizationTest = search.organizationsTestDataArray;

		for(let i =1;i<10;i++){
			if(organizationTest[i].name=name)
			{
				return organizationTest[i].name;
			}
			return '';
		}

	}

	search.getPropositionsOrganizations = function(){
		organizationsData.getDataCompareToPartOfName(search.writings).then(function(data)	
	    {	    	
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
	      
	      	search.organizationsTestDataArray=organizationData;
	      console.log(organizationData);
		}
}]);