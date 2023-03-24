// Countdown Timer

const allEvents = Array.from(document.querySelectorAll("is-desktop"));
console.log('Js Connected')
console.log('All events:'+allEvents)
function countDown(x) {
	if (x.matches) {
		console.log('Mobile');
	} else {
		// If media query matches
		console.log('Desktop');
		// Set the date we're counting down to
		var countDownDate = new Date('Mar 25, 2023 13:08:00').getTime();

		// Update the count down every 1 second
		var x = setInterval(function () {
			// Get today's date and time
			var now = new Date().getTime();

			// Find the distance between now and the count down date
			var distance = countDownDate - now;

			// Time calculations for days, hours, minutes and seconds
			var days = Math.floor(distance / (1000 * 60 * 60 * 24));
			var hours = Math.floor(
				(distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
			);
			var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
			var seconds = Math.floor((distance % (1000 * 60)) / 1000);

			// Output the result in an element with id="demo"
			document.getElementById('timer').innerHTML =
				days + 'd ' + hours + 'h ' + minutes + 'm ' + seconds + 's ';

			// If the count down is over, write some text
			if (distance < 0) {
				clearInterval(x);
				document.getElementById('timer').innerHTML = 'EXPIRED';
			}
		}, 1000);
	}
}

var x = window.matchMedia('(max-width: 768px)');
countDown(x); // Call listener function at run time
x.addListener(countDown); // Attach listener function on state changes

// Click to Copy
var tooltip = document.getElementById('myTooltip');
var copyText = document.getElementById('couponCode');
function myFunction() {
	copyText.select();
	copyText.setSelectionRange(0, 99999);
	document.execCommand('copy');
	tooltip.innerHTML = 'Copied: ' + copyText.value;
}
function outFunc() {
	tooltip.innerHTML = 'Copy to clipboard';
}

// Close
var closebtns = document.getElementsByClassName(
	'close'
); /* Get all elements with class="close" */
var i;
/* Loop through the elements, and hide the parent, when clicked on */
for (i = 0; i < closebtns.length; i++) {
	closebtns[i].addEventListener('click', function () {
		this.parentElement.style.display = 'none';
	});
}

var events = document.getElementsByClassName('is-timer');
for (i=0;i < events.length;i++){
	var countDownDate = new Date('Mar 25, 2023 13:08:00').getTime();
	var myfunc = setInterval(function() {

		var now = new Date().getTime();
		var timeleft = countDownDate - now;
			
		// Calculating the days, hours, minutes and seconds left
		var days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
		var hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		var minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((timeleft % (1000 * 60)) / 1000);

		this.document.getElementsByClassName('is-timer').innerHTML =
			days + 'd ' + hours + 'h ' + minutes + 'm ' + seconds + 's ';
			
		// Result is output to the specific element
		// document.getElementById("days").innerHTML = days + "d "
		// document.getElementById("hours").innerHTML = hours + "h " 
		// document.getElementById("mins").innerHTML = minutes + "m " 
		// document.getElementById("secs").innerHTML = seconds + "s " 
			
		// Display the message when countdown is over
		if (timeleft < 0) {
			clearInterval(myfunc);
			document.getElementById("days").innerHTML = ""
			document.getElementById("hours").innerHTML = "" 
			document.getElementById("mins").innerHTML = ""
			document.getElementById("secs").innerHTML = ""
			document.getElementById("end").innerHTML = "TIME UP!!";
		}
		}, 1000);
}
console.log(events)