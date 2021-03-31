function displayMessage(){
	const question = displayUserMessage();
	console.log(question);
	createDiv("user_message", question);
	displayPapyAnswer(question);
};

function createDiv(class_name, message){
	var new_div = document.createElement('div');
	new_div.className = class_name;
	var text = document.createTextNode(message);
	new_div.appendChild(text);
	display_message.appendChild(new_div);
};

function displayUserMessage(){
	var question = message_form.value;
	message_form.value = "";
	return question;
};

async function displayPapyAnswer(question){
	var spinner = document.getElementById('spinner');
	spinner.style.visibility = 'visible';
	await papyIsThinking(1, 8000);
	const url = new URL("http://127.0.0.1:5000/answer");
	const params = {'question': question}
	url.search = new URLSearchParams(params).toString();
	fetch(url)
	.then(resp => resp.json())
	.then((result) => {
		spinner.style.visibility = 'hidden';
		createDiv("papy_message", result.answer);
		if ("map" in result){
			addGoogleMap(result.map[0], result.map[1]);
			getWiki();
		}
	});
};

function initMap(lat, lng) {
	const place = { lat: lat, lng: lng };
	const map = new google.maps.Map(document.getElementById("map"), {
		zoom: 17,
		center: place,
	});
	const marker = new google.maps.Marker({
		position: place,
		map: map,
	});
}

function papyIsThinking(min, max){
	return new Promise(r => setTimeout(r, Math.random() * (max - min) + min));
}

function addGoogleMap(lat, lng){
	const div = document.createElement('div');
	div.id = 'map'
	const row = document.createElement('class');
	row.className = 'row mr-auto';
	const col = document.createElement('class');
	col.className = "offset-4 col-lg-8";
	div.style.visibility = 'visible';
	div.style.height = '200px';
	display_message.appendChild(row);
	row.appendChild(col);
	col.appendChild(div);
	initMap(lat, lng);
}

function getWiki(){
	const url = new URL("http://fr.wikipedia.org/w/api.php");
	const params = {"action": "query", "list": "search", "srsearch": "Cité Paradis Paris", "format":"json"};
	url.search = new URLSearchParams(params).toString();
	fetch(url, {
		method: "GET"
	})
	.then((resp) => {
		return resp.json();
	})
	.then((data) => {
		console.log(data.query.search[0]);
	})
};