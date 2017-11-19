angular.module('app.services')
    .service('CrawlService', ['$http', function CrawlService($http) {
        this.crawl = function(params) {
            return $http.get('api/crawler/crawl', {
            	params: params
            });
        };
    }]);