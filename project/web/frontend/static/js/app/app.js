angular.module('app.services', []);
angular.module('app.controllers', ['app.services']);

angular.module('app', ['ngRoute', 'app.controllers', 'app.services', 'angular-loading-bar'])
    .config(function($routeProvider){
        $routeProvider
            .when('/', {
            allowAnonymous: true,
            templateUrl: 'static/js/app/crawl/crawl.html',
            controller: 'CrawlCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    });
