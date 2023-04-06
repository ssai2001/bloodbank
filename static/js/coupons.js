//Create object with the list of due dates
//The 'name' will correspond to the field ID to populate the results
var cdates = document.getElementsByName('cdates')

// console.log(cdates)
var i;
var createdDate = {}

for (i=0;i < cdates.length;i++){
	var date = new Date(cdates[i].value).getTime();
	console.log(date)
	date = new Date(date + (60 * 24 * 60 * 60 * 1000))
	createdDate[i+4] = date
	console.log(date)
}
// var createdDate = {
//     '1':'2023-04-04 02:16:02',
//     '2':'2023-04-05 12:30:02',
// };

var timer = setInterval(function() {
    //Instantiate variables
    var dueDate, distance, days, hours, minutes, seconds, output;
    //Set flag to repeat function
    var repeat = false;
    // Get todays date and time
    var now = new Date().getTime();
    //Iterate through the due dates
    for (var dueDateId in createdDate)
    {
        //Get the due date for this record
        dueDate = new Date(createdDate[dueDateId]);
        // Find the distance between now an the due date
        distance = dueDate - now;
        // Time calculations for days, hours, minutes and seconds
        days    = Math.floor(distance  / (1000 * 60 * 60 * 24));
        hours   = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        seconds = Math.floor((distance % (1000 * 60)) / 1000);
        //Determine the output and populate the corresponding field
        if (distance > 0)
        {
            output = days + "d " + hours + "h " + minutes + "m " + seconds + "s";
            repeat = true; //If any record is not expired, set flag to repeat
        }
		else{
			output = "Expired"
		}
        document.getElementById(dueDateId).innerHTML = output;
        //If flag to repeat is false, clear event
		// clearInterval(timer);
        if(!repeat)
        {
            clearInterval(timer);
        }
    }
}, 1000);
 