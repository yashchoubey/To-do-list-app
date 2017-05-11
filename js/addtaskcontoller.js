
angular.module('toDoList').controller('addTaskController',["$timeout","$mdDialog","toDoService", function ($timeout,$mdDialog,toDoService) {
    /************************************** view *********************************************/
    var self = this;
    self.cancel = function () {
        $mdDialog.cancel();
    };
    self.save = function () {
        $mdDialog.hide(self.taskData);
    };
    /************************************** model *********************************************/
    self.category =[];
    /************************************** controller *********************************************/
    function initController(){
        self.showLoader=true;
        toDoService.getCategory().then(function(category){
            self.showLoader=false;
            self.category = category;
        });
    }
    initController();
}])