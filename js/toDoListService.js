
angular.module('toDoList')
    .factory('toDoService',function($q){
    /************************************** view *********************************************/
    var self = this;
    /************************************** model *********************************************/
   var category = {'Lunch':true,'Movies':false,'Grocery':false,'Shopping':false,'Rent':false};
    var taskList = [
        {
        title: 'title',
        description: 'description',
        category: 'Lunch',
        dueDate: new Date(),
        date: new Date()
        },
        {
        title: 'title1',
        description: 'description1',
        category: 'Movies',
        dueDate: new Date(),
        date: new Date()
        },
        {
        title: 'title2',
        description: 'description2',
        category: 'Lunch',
        dueDate: new Date(),
        date: new Date()
        }
    ];
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
            return $q.when(category);
        },
        getTaskList: function () {
            return $q.when(taskList);
        },
        getTaskData: function () {
            return $q.when(taskData);
        }
    }
})
