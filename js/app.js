
var toDoList=angular.module('toDoList', ['ngMaterial', 'ngMessages'])
    //*************************theme Portion******************************//
    .config(function ($mdThemingProvider) {
        $mdThemingProvider.theme('default')
            .primaryPalette('teal', {
                'default': '700',
                'hue-1': '100',
                'hue-2': '600',
                'hue-3': 'A200'
            })
            .accentPalette('amber', {
                'default': 'A400',
                'hue-1': '800'
            });
    })