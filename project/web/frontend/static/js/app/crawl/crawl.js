angular.module('app.controllers')
.controller('CrawlCtrl', ['$scope', '$location', 'CrawlService',
	function($scope, $location, CrawlService) {
	    $scope.info = {
	        url: null,
	        depth: null,
	        result: null
	    };

	    $scope.loading = false;
	    $scope.error = {
	    	status: false,
	    	message: null
	    };

	    $scope.submitForm = function() {
	        $scope.loading = true;

	        if(!$scope.info.url || $scope.info.url.length < 1) {
	        	$scope.error = {status: true, message: "A valid URL is required for the crawler."};
	        	$scope.loading = false;
	        	return;
	        }

	        if(!$scope.info.depth || isNaN($scope.info.depth)) {
	        	$scope.error = {status: true, message: "A number for depth is required for the crawler."};
	        	$scope.loading = false;
	        	return;
	        }

	        if($scope.info.url.indexOf("http://") !== 0 && $scope.info.url.indexOf("https://") !== 0) {
	        	$scope.info.url = "http://" + $scope.info.url;
	        }

	        CrawlService.crawl({ seed: $scope.info.url, depth: $scope.info.depth})
	        .then(function(result){
	            $scope.result = result.data.data;
	            $scope.loading = false;
	            $scope.error.status = false;
	        }, function(error){
	            $scope.loading = false;
	            $scope.error = {status: true, message: error.statusText};
	        });	        
	    };

	    $scope.dismiss = function() {
	    	$scope.error.status = false;	
	    };
	}
]);
