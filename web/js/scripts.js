var appname = angular.module('appname', []);
appname.controller('appCtrl', ['$scope', '$http', function($scope, $http) {
    $http.get("http://127.0.0.1:5000/api/getstatus").then(function(data){
        $scope.status = data.data;
    });
}]);