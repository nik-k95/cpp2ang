/**
 * Created by avrunev on 29.08.2016.
 */
angular.module('execAPI',[])
.factory('apiCiu', ['$http','$location', function($http,$location) {
        var apiUrl = 'https://api-dev.ciu.nstu.ru/v1.0/';
        var logoutUrl = '';

        var execFunc = function (funcName,params) {
            var payLoad = JSON.stringify(params);
            return $http.patch(apiUrl+'test/func/'+funcName, payLoad);
        };

        var execProc = function (procName,params) {
            var payLoad = JSON.stringify(params);
            return $http.patch(apiUrl+'test/proc/'+procName, payLoad);
        };

        var setURL = function (url,logout) {
            if (! url==null) {
                apiUrl = url;
                logoutUrl = logout;
            }
            else {
                //установка url-api на основе адреса загрузки
                var abs_url = $location.absUrl();
                var parser = document.createElement('a');
                parser.href = abs_url;
                var api_url = "";
                apiUrl = parser.protocol+"//"+parser.hostname+'/v1.0/';
                logoutUrl = parser.protocol+"//"+parser.hostname+'/v1.0/logout';
            };
        };

        var getLogoutURL = function () {
            return logoutUrl;
        };

        return {func:execFunc,proc:execProc,setURL:setURL,getLogoutURL:getLogoutURL};

}]);
