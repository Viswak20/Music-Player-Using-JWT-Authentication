$(document).ready(function() {
    $('#SignIn').on('click', function(e) {
        e.preventDefault();

        const Username = $('#email').val();
        const Password = $('#password').val();

        if (!Username) {
            alert('Enter the username');
            $('#email').focus();
        } else if (!Password) {
            alert('Enter the password');
            $('#password').focus();
        } else {
            $.ajax({
                url: '/api/login/',
                type: 'POST',
                data: JSON.stringify({
                    email: Username,
                    password: Password
                }),
                success: function (response) {
                    console.log(response.data);
                    // alert('Login successfully!');
                    // window.location.href = '/dashboard/';
                },
                error: function (xhr, status, error) {
                    alert('Login failed');
                }
            });
        }
    });
});