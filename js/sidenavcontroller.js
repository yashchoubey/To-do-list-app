
angular.module('toDoList').controller('sideNavController',["$mdSidenav","$mdDialog","toDoService", function ($mdSidenav,$mdDialog,toDoService) {
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
        delete self.category[categoryKey];
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
                if (self.category[categoryName] === undefined) {
                    self.category[categoryName] = false;
                }
                else
                {
                                //$mdDialog.show(
                                //    $mdDialog.alert()
                                //        .clickOutsideToClose(true)
                                //        .textContent('category is already defined.')
                                //        .ok('Got it!')
                                //);
                }
            }, function () {
            });
    }
    initController();
}]);