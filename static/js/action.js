$(document).ready(function(){
    $("#signup_form").validate({
        rules:{
            first_name: "required",
            last_name: "required",
            username: "required",
            email: {
                required: true,
                email: true
            },
            password:{
                required: true,
                minlength: 8
            },
            password2:{
                required: true,
                equalTo: "#pw"
            }
        },
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            username: "Please enter your username",
            email: "Please enter a valid email address",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 8 characters long"
            },
            password2: {
                required: "Please provide a password",
                equalTo: "Please input same password"
            }
        }
    });
});
