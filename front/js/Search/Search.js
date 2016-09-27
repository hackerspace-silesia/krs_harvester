  angular.module('Data')
  .controller('SearchCtr',['organizationsData','$window',function ( organizationsData, $window) 
{	
	var search=this;

	search.sum="557 563 428";
	search.organizationsNames = {};
	search.writings='';

	search.checkIsWritingsCorrect=function(){
	
		if(isNameExist()){

			showOrganizationPage(search.writings);
		}
		else
		{
			//TODO
			alert('Nieprawidłowe dane');
		}
	}

	showOrganizationPage = function(id){

		$window.location.assign('#/organisation/'+id+'/');
	}

	isNameExist = function(){	

		for(let i = 0;i<10;i++){
			if(search.organizationsNames[i].name==search.writings)
			{console.log(search.writings);
				return true;
			}
		}
		return false;
	}

	search.getPropositionsOrganizations = function(){
		organizationsData.getDataCompareToPartOfName(search.writings).then(function(data)	
	    {console.log(search.writings);
	    	search.organizationsNames =	getPropositionsOrganizationsNames(data);    		    	
	    });
	}

	var getPropositionsOrganizationsNames = function (arrayOfObjectOrganisations)
	{	
		let data = arrayOfObjectOrganisations;
		let organizationData = {};
	
	      	for(let i=0;i<10;i++){
	      		if(typeof data[i] =='object')
	      		{
		      		let id = data[i].pk;
		      		organizationData[i]={'name':{}};
		      		organizationData[i]['name']=data[i].name;
	      		}
	      	}
	      	return organizationData;
		}
}]);