// console.log('Js Working')
function validate(){
    const hospital_name = document.getElementById('hospital_name').value;
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const contact = document.getElementById('contact').value;
    const password = document.getElementById('password').value;
    const password2 = document.getElementById('password2').value;
    console.log('hospital name:' + hospital_name.length )

    let error = false
    
    // Validation for hospital_name.
    if(hospital_name === ""){
        error = true
        document.getElementById('hospital_name_error').innerHTML = 'Hospital-Name is required.'
        document.getElementById('hospital_name').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('hospital_name_error').innerHTML = ''
        document.getElementById('hospital_name').setAttribute("class","form-control is-valid")
    }

    // Username Validation.{HID-DD-MM-YYYY-SLNO}
    if(username === ""){
        error = true
        document.getElementById('username_error').innerHTML = 'Username is required.'
        document.getElementById('username').setAttribute("class","form-control is-invalid")
    }
    else if(username.length != 18){
        error = true
        document.getElementById('username_error').innerHTML = 'Invalid Username'
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

    //contact no validation
    if(contact === ""){
        error = true
        document.getElementById('contact_error').innerHTML = 'Contact No. is required.'
        document.getElementById('contact').setAttribute("class","form-control is-invalid")
    }
    else if(contact.length != 10){
        error = true
        document.getElementById('contact_error').innerHTML = 'Please enter a valid Contact No.'
        document.getElementById('contact').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('contact_error').innerHTML = ''
        document.getElementById('contact').setAttribute("class","form-control is-valid")
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