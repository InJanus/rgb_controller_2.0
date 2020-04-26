var myApp = angular.module('myApp', []);

myApp.controller('textCtrl', function textCtrl($scope, $http){
    $http.get('http://127.0.0.1:5000/api/getstatus').then(function(data){
        $scope.photos = data.data;
    });
});
    