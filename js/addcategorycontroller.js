
angular.module('toDoList').controller('addCategoryController',["$timeout","$mdDialog","toDoService", function ($timeout,$mdDialog,toDoService) {
    /************************************** view *********************************************/
    var self = this;
    self.cancel = function () {
        $mdDialog.cancel();
    };
    self.save = function () {
        $mdDialog.hide(self.categoryName);
    };
    self.checkDuplicate = function (categoryName) {
        checkDuplicateKey(categoryName);
    };
    /************************************** model *********************************************/
    self.categoryName='';
    self.message='';
    self.category = {};
   /************************************** controller *********************************************/
   function initController(){
       self.showLoader=true;
       toDoService.getCategory().then(function(category){
           self.showLoader=false;
           self.category = category;
       });
   }
    function checkDuplicateKey(categoryName)
    {
        if (self.category[categoryName] !== undefined) {
            self.message='category is already defined!'
        }
    }
    initController();
}])