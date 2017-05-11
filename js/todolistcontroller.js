
angular.module('toDoList').controller('toDoListController',["$mdDialog","toDoService", function ($mdDialog,toDoService) {
    /************************************** view *********************************************/
    var self = this;
    self.deleteTask = function(ev) {
        deleteTask(ev);
    };
    self.addTask = function(ev) {
        addTask(ev);
    };
    /************************************** model *********************************************/
    self.taskList=[];
    self.category =[];
    self.todayDate=new Date();
    /************************************** controller *********************************************/
    function initController(){
        self.showLoader=true;
        toDoService.getTaskList().then(function(taskList){
            self.showLoader=false;
            self.taskList = taskList;
        });
        toDoService.getCategory().then(function(category){
            self.showLoader=false;
            self.category = category;
        });
    }
    function addTask(ev) {
        $mdDialog.show({
            controller: 'addTaskController',
            controllerAs:'addTaskCtrl',
            templateUrl: 'views/addtaskview.html',
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true
        })
            .then(function (taskData) {

                self.taskList.push(taskData);
                self.taskList.date=new Date();
            }, function () {
                self.status = 'Task is discarded.';
            });
    }
    function deleteTask(taskobj){
        var index = self.taskList.indexOf(taskobj);
        self.taskList.splice(index, 1);
    }
    initController();
}])