angular.module('app', ['Tracks','ngRoute']).
config(function ($routeProvider) 
{
	$routeProvider.when('/trasy', {
		templateUrl: 'views/main.html', controller: 'TracksController'});
	$routeProvider.when('/organisation', {
		templateUrl: 'views/organisation.html', controller: 'TracksController'});
	$routeProvider.otherwise({
	redirectTo: '/trasy'
	});
});
angular.module('Tracks', []);