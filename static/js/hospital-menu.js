console.log('linked')
var incrementButton = document.getElementsByClassName('inc')
var decrementButton = document.getElementsByClassName('dec')

// console.log(incrementButton)

for(var i=0;i < incrementButton.length; i++){
    var button = incrementButton[i];
    button.addEventListener('click',function(event){
        var buttonClicked = event.target;
        var input = buttonClicked.parentElement.children[1]
        var inputValue = input.value
        if(inputValue < 20){
            var newValue = parseInt(inputValue) + 1
            input.value = newValue
        }
        else{
            alert('Quantity cannot be more than 20')
        }
    })
}

for(var i=0;i < decrementButton.length; i++){
    var button = decrementButton[i];
    button.addEventListener('click',function(event){
        var buttonClicked = event.target;
        var input = buttonClicked.parentElement.children[1]
        var inputValue = input.value
        if(inputValue > 1){
            var newValue = parseInt(inputValue) - 1
            input.value = newValue
        }
        else{
            alert('Quantity cannot be less than 1')
        }
    })
}