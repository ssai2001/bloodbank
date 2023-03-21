var today = new Date().toISOString().split('T')[0];
document.getElementById("date").value = today;
document.getElementById("date").setAttribute('min', today);
function validateOrganizer(){
    const organizationName = document.getElementById('organizationName').value;
    const fullname = document.getElementById('fullname').value;
    const email = document.getElementById('email').value;
    const date = document.getElementById('date').value;
    const shortDescription = document.getElementById('shortDescription').value;

    let error = false;

    //organizationName validation
    if(organizationName.trim() === ""){
        error = true
        document.getElementById('organizationName_error').innerHTML = 'Organization Name is required.'
        document.getElementById('organizationName').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('organizationName_error').innerHTML = ''
        document.getElementById('organizationName').setAttribute("class","form-control is-valid")
    }

    //fullname validation
    if(fullname.trim() === ""){
        error = true
        document.getElementById('fullname_error').innerHTML = 'Full Name is required.'
        document.getElementById('fullname').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('fullname_error').innerHTML = ''
        document.getElementById('fullname').setAttribute("class","form-control is-valid")
    }

    //email validation
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

    //date validation

    //description validation
    if(shortDescription.trim() === ""){
        error = true
        document.getElementById('shortDescription_error').innerHTML = 'Please give short description about the program'
        document.getElementById('shortDescription').setAttribute("class","form-control is-invalid")
    }
    else if(shortDescription.trim().length < 15){
        error = true
        document.getElementById('shortDescription_error').innerHTML = 'Please give short description about the program'
        document.getElementById('shortDescription').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('shortDescription_error').innerHTML = ''
        document.getElementById('shortDescription').setAttribute("class","form-control is-valid")
    }

    if(error){
        return false;
    }
    else{
        return true;
    }
}