function validate(){
    const username = document.getElementById('username').value
    const password = document.getElementById('password').value

    let error = false

    if(username === ""){
        error = true
        document.getElementById('username_error').innerHTML = 'SIC number is required.'
        document.getElementById('username').setAttribute("class","form-control is-invalid")
    }
    else if(username.length < 6 || username.length > 16){
        error = true
        document.getElementById('username_error').innerHTML = 'Username must be 6-16 characters long'
        document.getElementById('username').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('username_error').innerHTML = ''
        document.getElementById('username').setAttribute("class","form-control is-valid")
    }

    if(password === ""){
        error = true
        document.getElementById('password_error').innerHTML = "Password is required."
        document.getElementById('password').setAttribute("class","form-control is-invalid")
    }
    else if(password.length < 8 || password.length > 16){
        error = true
        document.getElementById('password_error').innerHTML = "Password must be 8-16 characters long."
        document.getElementById('password').setAttribute("class","form-control is-invalid")
    }
    else if(!password.match(/[a-z]/)){
        error = true
        document.getElementById('password_error').innerHTML = "Password must contain at-least one lowercase character"
        document.getElementById('password').setAttribute("class","form-control is-invalid")
    }
    else if(!password.match(/[A-Z]/)){
        error = true
        document.getElementById('password_error').innerHTML = "Password must contain at-least one uppercase character"
        document.getElementById('password').setAttribute("class","form-control is-invalid")
    }
    else if(!password.match(/[0-9]/)){
        error = true
        document.getElementById('password_error').innerHTML = "Password must contain at-least one numeric character"
        document.getElementById('password').setAttribute("class","form-control is-invalid")
    }
    else if(!password.match(/[~!@#$%^&*]/)){
        error = true
        document.getElementById('password_error').innerHTML = "Password must contain at-least one special character"
        document.getElementById('password').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('password_error').innerHTML = ""
        document.getElementById('password').setAttribute("class","form-control is-valid")
    }

    if(error){
        return false
    }
    else{
        return true
    }
}