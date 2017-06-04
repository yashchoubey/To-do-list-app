angular.module('toDoList')
    .factory('toDoService',function($q,$http){
    /************************************** view *********************************************/
    var self = this;
    /************************************** model *********************************************/
    
    var taskData = {
        title: '',
        description: '',
        category: '',
        dueDate: new Date(),
        date: new Date()
    };
    /************************************** controller *********************************************/
    return {
        getCategory:function(){
            return $http.get('/todo/category').then(function (response) {return response.data;});
        },
        getTaskList: function () {
            return $http.get('/todo/todolist').then(function (response) {return response.data;});
        },
        getTaskData: function () {
            return $q.when(taskData);
        }
    }
})
