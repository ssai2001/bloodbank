function validate(){
    const first_name = document.getElementById('first_name').value;
    const last_name = document.getElementById('last_name').value;
    const username = document.getElementById('username').value;
    const BloodGroup = document.getElementById('BloodGroup').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const password2 = document.getElementById('password2').value;
    console.log('First name:' + first_name.length )

    let error = false
    
    // Validation for first_name.
    if(first_name === ""){
        error = true
        document.getElementById('first_name_error').innerHTML = 'First-Name is required.'
        document.getElementById('first_name').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('first_name_error').innerHTML = ''
        document.getElementById('first_name').setAttribute("class","form-control is-valid")
    }

    // Last_Name Validation
    if(last_name === ""){
        error = true
        document.getElementById('last_name_error').innerHTML = 'Last-Name is required.'
        document.getElementById('last_name').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('last_name_error').innerHTML = ''
        document.getElementById('last_name').setAttribute("class","form-control is-valid")
    }

    //Blood Group Validation
    if(BloodGroup === ""){
        error = true
        document.getElementById('blood_group_error').innerHTML = 'Blood Group is required.'
        document.getElementById('BloodGroup').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('blood_group_error').innerHTML = ''
        document.getElementById('BloodGroup').setAttribute("class","form-control is-valid")
    }

    // Username Validation
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

    // email validation
    let atPos = email.indexOf('@')
    let dotPos = email.indexOf('.')
    if(email === ""){
        error = true
        document.getElementById('email_error').innerHTML = "E-mail is required."
        document.getElementById('email').setAttribute("class","form-control is-invalid")
    }
    else if((atPos<=0) || (dotPos<=0) || (dotPos-atPos<=4) || (dotPos==email.length-1) || (atPos==0)){
        error = true
        document.getElementById('email_error').innerHTML = "Please enter a valid E-mail"
        document.getElementById('email').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('email_error').innerHTML = ""
        document.getElementById('email').setAttribute("class","form-control is-valid")
    }

    // Password validation
    console.log(password.length)
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

    // Confirm Password validation
    if(password2 === ""){
        error = true
        document.getElementById('password2_error').innerHTML = "Confirm Password is required."
        document.getElementById('password2').setAttribute("class","form-control is-invalid")
    }
    else if(password != password2){
        error = true
        document.getElementById('password2_error').innerHTML = "Password & Confirm Password doesn't match."
        document.getElementById('password2').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('password2_error').innerHTML = ""
        document.getElementById('password2').setAttribute("class","form-control is-valid")
    }

    if(error){
        return false;
    }
    else{
        return true;
    }
}