function displayMessage(){
	//get the question and display
	const question = message_form.value;
	message_form.value = "";
	createDiv("user_message", question);
	displayPapyAnswer(question);
};

function createDiv(class_name, message){
	//create dialogue bubble
	var new_div = document.createElement('div');
	new_div.className = class_name;
	var text = document.createTextNode(message);
	new_div.appendChild(text);
	display_message.appendChild(new_div);
};

async function displayPapyAnswer(question){
	// get papy answer and display
	var spinner = document.getElementById('spinner');
	spinner.style.visibility = 'visible';
	await papyIsThinking(1, 8000);
	const url = new URL("http://127.0.0.1:5000/answer");
	const params = {'question': question}
	url.search = new URLSearchParams(params).toString();
	const result = await fetch(url).then(resp => resp.json())
	spinner.style.visibility = 'hidden';
	createDiv("papy_message", result.answer.papy);
	if ("location" in result.answer){
		addGoogleMap(result.answer.location.lat, result.answer.location.lng);
		createDiv("papy_message", result.answer.wiki);
	}
	else if ("movie" in result.answer){
		createDiv("papy_message", result.answer.movie);
	}
	else if ("book" in result.answer){
		createDiv("papy_message", result.answer.book);
	}
};

function initMap(lat, lng, id) {
	// initialize google map with the requested place
	const place = { lat: lat, lng: lng };
	const map = new google.maps.Map(document.getElementById(id), {
		zoom: 17,
		center: place,
	});
	const marker = new google.maps.Marker({
		position: place,
		map: map,
	});
}

function papyIsThinking(min, max){
	// set a delay between the question and the answer
	return new Promise(r => setTimeout(r, Math.random() * (max - min) + min));
}

function addGoogleMap(lat, lng){
	// display google map in the chat
	const div = document.createElement('div');
	const date = new Date();
	const actualTime = date.getFullYear() + '-' + date.getMonth() + '-' + date.getDate() + '-' + 
	date.getHours() + '-' + date.getMinutes() + '-' + date.getSeconds();
	div.id = `map-${actualTime}`
	const row = document.createElement('class');
	row.className = 'row mr-auto';
	const col = document.createElement('class');
	col.className = "offset-4 col-lg-8";
	div.style.visibility = 'visible';
	div.style.height = '200px';
	display_message.appendChild(row);
	row.appendChild(col);
	col.appendChild(div);
	initMap(lat, lng, div.id);
}
