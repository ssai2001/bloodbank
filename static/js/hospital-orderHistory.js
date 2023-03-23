console.log('Js Linked')

var status = document.getElementById('status').value
console.log(status)

if(status){
    document.getElementById('card').setAttribute("class","card bg-success")
}
else{
    document.getElementById('card').setAttribute("class","card bg-warning")
}