$(document).ready(function() {
	setupEditor();
	$("#loadingIcon").toggle();	
});

function setupEditor() {
	var editor = ace.edit("editor");
	editor.getSession().setMode("ace/mode/c_cpp");
	editor.resize();

	var solutionEditor = ace.edit("solutionEditor");
	solutionEditor.getSession().setMode("ace/mode/c_cpp");
	solutionEditor.resize();
}

function toggleUISubmit(isOn) {
	if (isOn) {
		$("#loadingIcon").toggle();
		document.getElementById("submitCode").disabled = true;
	}
	else {
		$("#loadingIcon").toggle();
		document.getElementById("submitCode").disabled = false;		
	}
}

function onSubmitCode() {
	var url = '/cs/submitCode';
	var editor = ace.edit("editor");

	var data = {
		code : editor.getValue()
	};

	$.getJSON(url, data, onSubmitCodeResults);

	// Disable UI
	toggleUISubmit(true);
}

function onSubmitCodeResults(data) {
	document.getElementById("executeResults").innerHTML = data.executeResults;
	document.getElementById("compileResults").innerHTML = data.compileResults;

	// Enable UI
	toggleUISubmit(false)
}
