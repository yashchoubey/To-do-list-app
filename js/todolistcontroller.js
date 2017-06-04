
angular.module('toDoList').controller('toDoListController',["$mdDialog","toDoService","$http", function ($mdDialog,toDoService,$http) {
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
                console.log(taskData)
                console.log(taskData.title)
                var sendJSON = {};
                sendJSON.name=taskData.title;
                sendJSON.category=taskData.category;
                sendJSON.dateTime=taskData.dueDate;
                sendJSON.description=taskData.description;
                //sendJSON.userName=username;
                $http.put('/todo/todolist', sendJSON).then(function (response) {console.log("task added");initController();});

            }, function () {
                self.status = 'Task is discarded.';
            });
    }
    function deleteTask(taskobj){
        var index = self.taskList.indexOf(taskobj);
        self.taskList.splice(index, 1);

        console.log(taskobj)
        var sendJSON = {};
        sendJSON.categoryName=categoryKey;
        //sendJSON.userName=username;
        $http.delete('/todo/todolist', {params: sendJSON}).then(function (response) {console.log("deleted");initController();});



    }
    initController();
}])