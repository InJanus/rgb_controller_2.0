var appname = angular.module('appname', []);
appname.controller('appCtrl', ['$scope', '$http', function($scope, $http) {
    $http.get("http://127.0.0.1:5000/api/getstatus").then(function(data){
        console.log(data.data);
        $scope.color = {'red':0,'green':0,'blue':0};
        if(data.data.status){
            //color block green
            $scope.status = true;

        }else{
            $scope.status = false;
        }
        var mystep = 255.0/100.0;
        if(data.data.color.red){
            $scope.color.red = Math.round(mystep*data.data.color.red);
        }else{
            $scope.color.red = 0;
        }
        if(data.data.color.green){
            $scope.color.green = Math.round(mystep*data.data.color.green);
        }else{
            $scope.color.green = 0;
        }
        if(data.data.color.blue){
            $scope.color.blue = Math.round(mystep*data.data.color.blue);
        }else{
            $scope.color.blue = 0;
        }
        $scope.updatecolor();
        
    });
    $scope.updatecolor = function(){
        var rgbval = "rgb(" + String($scope.color.red) + "," + String($scope.color.green) + "," + String($scope.color.blue) + ")";
        console.log(rgbval);
        document.getElementById("viewColor").style.backgroundColor = rgbval;
    }
    $scope.changecolor = function(){
        var color = document.getElementById("html5colorpicker").value;
        var rgb = HEX2RGB(color)
        $http.post("http://127.0.0.1:5000/api/color", rgb).then(function(data){
            console.log(data.data);
        });
    }
}]);

function HEX2RGB (hex) {
    "use strict";
    if (hex.charAt(0) === '#') {
        hex = hex.substr(1);
    }
    if ((hex.length < 2) || (hex.length > 6)) {
        return false;
    }
    var values = hex.split(''),
        r,
        g,
        b;

    if (hex.length === 2) {
        r = parseInt(values[0].toString() + values[1].toString(), 16);
        g = r;
        b = r;
    } else if (hex.length === 3) {
        r = parseInt(values[0].toString() + values[0].toString(), 16);
        g = parseInt(values[1].toString() + values[1].toString(), 16);
        b = parseInt(values[2].toString() + values[2].toString(), 16);
    } else if (hex.length === 6) {
        r = parseInt(values[0].toString() + values[1].toString(), 16);
        g = parseInt(values[2].toString() + values[3].toString(), 16);
        b = parseInt(values[4].toString() + values[5].toString(), 16);
    } else {
        return false;
    }
    return {'red':r,'green': g,'blue': b};
}