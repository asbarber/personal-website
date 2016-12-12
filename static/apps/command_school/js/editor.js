$(document).ready(function() {
	setupEditor();
});

function setupEditor() {
	var editor = ace.edit("editor");
	editor.getSession().setMode("ace/mode/c_cpp");
	editor.resize();
}

function onSubmitCode() {
	var url = '/cs/submitCode';
	var idSubmit = '#submitCode';
	var editor = ace.edit("editor");

	var data = {
		code : editor.getValue()
	};

	$.getJSON(url, data, onSubmitCodeResults);
}

function onSubmitCodeResults(data) {
	document.getElementById("codeResults").innerHTML = data.runResults;
}

