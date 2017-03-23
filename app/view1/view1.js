'use strict';

angular.module('myApp.view1', ['ngRoute','execAPI'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/view1', {
            templateUrl: 'view1/view1.html',
            controller: 'View1Ctrl'
        });
    }])

    .controller('View1Ctrl', ['$scope', '$http', '$interval','$sce','apiCiu', function ($scope, $http, $interval, $sce, apiCiu) {

        $scope.trustAsHtml = function(value) {
            return $sce.trustAsHtml(value);
        };

        $scope.current_level = {};

        apiCiu.func('decanatuser.ohop_on_site_pkg.get_levels',{}).success(
            function (data) {
                $scope.data_levels = data;
            }
        );

        $scope.curr_grdOptions = {
            enableRowSelection: true,
            enableRowHeaderSelection: false,
            multiSelect: false,
            modifierKeysToMultiSelect: false,
            noUnselect: true,
            enableFiltering: true,
            columnDefs:  [
                { field: 'ID_CURRICULUM', displayName: '№', maxWidth: 80},
                { field: 'OKSO_STR', displayName: 'Направление' },
                { field: 'PROFILE_DIRECTION' , displayName: 'Профиль' },
                { field: 'FACULTET' , displayName: 'Факультет', maxWidth: 100 },
                { field: 'YEAR_ENROL', displayName: 'Год', maxWidth: 80}
            ],
        onRegisterApi: function (gridApi) {
                $scope.curr_grdApi = gridApi;
            }
        };


        apiCiu.func('decanatuser.ohop_on_site_pkg.get_currs',[0,0]).success(
            function (data) {
               $scope.curr_grdOptions.data = data;
            }
        );

        $scope.files_grdOptions = {
            enableRowSelection: true,
            enableRowHeaderSelection: false,
            multiSelect: false,
            modifierKeysToMultiSelect: false,
            noUnselect: true,
            enableFiltering: true,
            columnDefs:  [
                { field: 'NAME', displayName: 'Тип', minWidth: 120},
                { field: 'PUBLISH_DATE', displayName: 'Дата загрузки' }
            ],
            onRegisterApi: function (gridApi) {
                $scope.files_grdApi = gridApi;
    }
        };

        $scope.curr_grdClick = function(){
            var rows = $scope.curr_grdApi.selection.getSelectedRows();
            $scope.id_curriculum = rows[0]["ID_CURRICULUM"];
            apiCiu.func('decanatuser.ohop_on_site_pkg.get_curr_files',[$scope.id_curriculum]).success(
                function (data) {
                    $scope.files_grdOptions.data = data;
                }
            );
        }

    }]).filter('propsFilter', function () {
    //фильтрация в выпадающем списке
    return function (items, props) {
        var out = [];

        if (angular.isArray(items)) {
            var keys = Object.keys(props);

            items.forEach(function (item) {
                var itemMatches = false;

                for (var i = 0; i < keys.length; i++) {
                    var prop = keys[i];
                    var text = props[prop].toLowerCase();
                    if (item[prop].toString().toLowerCase().indexOf(text) !== -1) {
                        itemMatches = true;
                        break;
                    }
                }

                if (itemMatches) {
                    out.push(item);
                }
            });
        } else {
            // Let the output be the input untouched
            out = items;
        }

        return out;
    };
});