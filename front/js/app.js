angular.module('app', ['Charts','ngRoute']).
config(function ($routeProvider) 
{
	$routeProvider.when('/main', {
		templateUrl: 'views/main.html'});
	$routeProvider.when('/organisation', {
		templateUrl: 'views/organisation.html', controller:'LineCtrl'});
	$routeProvider.otherwise({
	redirectTo: '/main'
	});
});
angular.module('Charts', []);