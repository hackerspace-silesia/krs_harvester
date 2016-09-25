let app = angular.module('app', ['Data','ngRoute','restangular','ChartCity', 'MapWojewodztwa']);
app.config(function ($routeProvider) 
{
	$routeProvider.when('/main', {
		templateUrl: 'views/main.html'});
	$routeProvider.when('/organisation/:name', {
		templateUrl: 'views/organisation.html'});
  $routeProvider.when('/chart/city', {
    templateUrl: 'views/ChartCity.html'});
  $routeProvider.when('/chart/wojewodztwa', {
    templateUrl: 'views/MapWojewodztwa.html'});
	$routeProvider.otherwise({
	  redirectTo: '/main'
	});


})
// Configure the application
app.config(function(RestangularProvider) {

    // add a response intereceptor
   RestangularProvider.setRequestSuffix('/');
   RestangularProvider.setBaseUrl('http://127.0.0.1:8000/api/');
   RestangularProvider.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
      var extractedData;
      if (operation === "getList") {
        extractedData = data.results;
      } else {
        extractedData = data;
        console.log(data);
      }
      return extractedData;
    });

});

angular.module('Data', []);
