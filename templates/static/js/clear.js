function clearFields() {
	let input = document.getElementById('inText').value
	let output = document.getElementById('outText').value

	if (input) {
		document.getElementById('inText').innerHTML = ""
	}

	if (output){
		document.getElementById('outText').innerHTML = ""
	}
}
