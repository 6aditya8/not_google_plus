(function () {
    'use strict';

    angular
        .module('thinkster.authentication.services')
        .factory('Authentication',Authentication);
    
    Authentication.$inject = ['$http','$cookies'];

    function Authentication($http, $cookies) {
        var Authentication = {
            register: register
        };
        return Authentication;
    }

    function register(email, password, username) {
        return $http.post ('/accounts/', {
            username: username,
            password: password,
            email: email
        })
    }
})();