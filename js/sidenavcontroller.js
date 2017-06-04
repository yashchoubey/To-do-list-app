
angular.module('toDoList').controller('sideNavController',["$mdSidenav","$mdDialog","toDoService","$http", function ($mdSidenav,$mdDialog,toDoService,$http) {
    /************************************** view *********************************************/
    var self=this;
    self.deleteCategory = function(categoryKey) {
        deleteCategory(categoryKey);
    };
    self.addCategory = function(ev) {
        addCategory(ev);
    };
    /************************************** model *********************************************/
    self.toggleLeft = buildToggler('left');
    self.toggleRight = buildToggler('right');
    self.category = {};
    self.showLoader=false;
    /************************************** controller *********************************************/
    function initController(){
        self.showLoader=true;
        toDoService.getCategory().then(function(category){
            self.showLoader=false;
            self.category = category;
        });
    }
    function buildToggler(componentId) {
        return function () {
            $mdSidenav(componentId).toggle();
        }
    }
    function deleteCategory(categoryKey){
        //delete self.category[categoryKey];
        var sendJSON = {};
        sendJSON.categoryName=categoryKey;
        //sendJSON.userName=username;
        $http.delete('/todo/category', {params: sendJSON}).then(function (response) {console.log("deleted");initController();});
    }
    function addCategory(ev){
        $mdDialog.show({
            controller: 'addCategoryController',
            controllerAs:'addCategoryCtrl',
            templateUrl: 'views/addcategoryview.html',
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true
        })
            .then(function (categoryName) {
                var sendJSON = {};
                sendJSON.categoryName=categoryName;
                //sendJSON.userName=username;
                //$http.post('/todo/category', {params: sendJSON}).then(function (response) {console.log("added");initController();});
                $http.post('/todo/category?categoryName='+categoryName).then(function (response) {console.log("added");initController();});
            }, function () {
            });
    }
    initController();
}]);